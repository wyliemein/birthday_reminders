# Generated by Django 3.1.5 on 2021-02-12 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='owner_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='birthdays.user'),
            preserve_default=False,
        ),
    ]
