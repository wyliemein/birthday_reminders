from django.db import models
from django.conf import settings
import redis
import datetime
import uuid


# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Contact(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    phone_number = models.CharField(max_length=20)
    birthday = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_id = models.CharField(max_length=50, blank=True, editable=False, unique=True, null=True, default=None)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def schedule_message(self):
    # Calculate the correct time to send this reminder
        now_time_date = datetime.datetime.utcnow()
        offset = datetime.timedelta(hours=8)
        current_time_date = now_time_date - offset
        current_date = current_time_date.date()
        print('current datetime: ', current_time_date)
        self.birthday = self.birthday.replace(year=current_date.year)
        if self.birthday < current_date: 
            self.birthday = self.birthday.replace(year=current_date.year+1)
        message_time_date = datetime.datetime.combine(self.birthday, self.time)
        print('message datetime: ', message_time_date)
        if current_time_date.time() > message_time_date.time():
            time_to_message = datetime.timedelta(minutes=1)
            print("time has passed sending in: ",time_to_message)
        else:
            time_to_message = message_time_date - current_time_date
        time_of_message = time_to_message.total_seconds()
        print('time to message on day in seconds: ', time_of_message)
        # to get time in seconds:
        milli_to_wait = int(
            (time_of_message)) * 1000
        print(milli_to_wait)
        # Schedule the Dramatiq task
        from .tasks import send_sms_reminder
        result = send_sms_reminder.send_with_options(
            args=(self.pk,),
            delay=milli_to_wait)
        print(result.options)
        return result.options['redis_message_id']

    def save(self, *args, **kwargs):
        """Custom save method which also schedules a reminder"""
        # Check if we have scheduled a reminder for this appointment before
        if self.task_id:
            # Revoke that task in case its time has changed
            self.cancel_message()
            super(Contact, self).delete(*args, **kwargs)

        # Save our appointment, which populates self.pk,
        # which is used in schedule_reminder
        if self.pk is None:
            super(Contact, self).save(*args, **kwargs)
            self.task_id = self.schedule_message()
        else:
            self.task_id = self.schedule_message()
        # Schedule a new reminder task for this appointment
        # Save our appointment again, with the new task_id
            super(Contact, self).save(*args, **kwargs)

    def cancel_message(self):
        redis_client = redis.from_url(settings.REDIS_URL)
        redis_client.hdel("dramatiq:default.DQ.msgs", self.task_id)