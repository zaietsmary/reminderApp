from celery import Celery
from celery.schedules import crontab

app = Celery('reminder_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'Europe/Kyiv'
app.conf.enable_utc = False

app.conf.beat_schedule = {
    'send-reminder-every-day-at-midnight': {
        'task': 'app.tasks.send_reminder',
        'schedule': crontab(hour=0, minute=0),
    },
}
