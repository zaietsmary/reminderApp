from django.db import models
from django.urls import reverse

class Reminder(models.Model):
    info = models.CharField(
        'Текст нагадування',
        max_length=200,
        help_text='Максимум 200 символів'
    )
    date = models.DateTimeField('Дата та час нагадування')
    email = models.EmailField('Email отримувача', default='', help_text='Вкажіть email для нагадування')
    sent = models.BooleanField('Надіслано', default=False)

    class Meta:
        verbose_name = 'Нагадування'
        verbose_name_plural = 'Нагадування'

    def __str__(self):
        return self.info
