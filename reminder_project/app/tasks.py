from celery import shared_task
from .models import Reminder
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

@shared_task
def send_reminder(reminder_id):
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        send_mail(
            subject='Reminder',
            message=reminder.info,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[reminder.email],
        )
        reminder.sent = True
        reminder.save()
    except ObjectDoesNotExist:
        print(f"Reminder {reminder_id} does not exist")
