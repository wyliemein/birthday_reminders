from __future__ import absolute_import

import dramatiq

from django.conf import settings
from twilio.rest import Client

from .models import Contact


# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@dramatiq.actor
def send_sms_reminder(contact_id):
    """Send a reminder to a phone using Twilio SMS"""
    # Get our contact from the database
    print("sending... ", contact_id)
    try:
        contact = Contact.objects.get(pk=contact_id)
    except Contact.DoesNotExist:
        # The contact we were trying to remind someone about
        # has been deleted, so we don't need to do anything
        return
    body = contact.message
    client.messages.create(
        body=body,
        to=contact.phone_number,
        from_=settings.TWILIO_NUMBER,
    )
