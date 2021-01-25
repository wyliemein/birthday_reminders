from django.db import models
from django.conf import settings
import arrow
import redis
import datetime
import ciso8601
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
    task_id = models.CharField(max_length=50, blank=True, editable=False, default=str(uuid.uuid1))

    def __str__(self):
        return self.name

    def schedule_message(self):
    # Calculate the correct time to send this reminder
        message_time = self.time
        now = datetime.date.today()
        self.birthday = self.birthday.replace(year=now.year)
        if self.birthday < now: 
            self.birthday = self.birthday.replace(year=now.year+1)
        time_to_birthday = abs(self.birthday - now)
        time_seconds = time_to_birthday.days * 24 * 60 * 60
        time_of_message = self.time.hour * 3600 + self.time.minute * 60 + self.time.second
        # to get time in seconds:
        milli_to_wait = int(
            (time_seconds + time_of_message)) * 1000

        # Schedule the Dramatiq task
        from .tasks import send_sms_reminder
        result = send_sms_reminder.send_with_options(
            args=(self.pk,),
            delay=milli_to_wait)

        return result.options['redis_message_id']

    def save(self, *args, **kwargs):
        """Custom save method which also schedules a reminder"""

        # Check if we have scheduled a reminder for this appointment before
        if self.task_id:
            # Revoke that task in case its time has changed
            self.cancel_message()

        # Save our appointment, which populates self.pk,
        # which is used in schedule_reminder
        super(Contact, self).save(*args, **kwargs)

        # Schedule a new reminder task for this appointment
        self.task_id = self.schedule_message()

        # Save our appointment again, with the new task_id
        super(Contact, self).save(*args, **kwargs)

    def cancel_message(self):
        redis_client = redis.Redis(host=settings.REDIS_LOCAL, port=6379, db=0)
        redis_client.hdel("dramatiq:default.DQ.msgs", self.task_id)