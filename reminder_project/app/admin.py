from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('info', 'date')
    search_fields = ('info',)
    fieldsets = (
        ('Основне', {
            'fields': ('info', 'date', 'email'),
        }),
    )
    def formatted_date(self, obj):
        return obj.date.strftime('%d.%m.%Y %H:%M')
    formatted_date.admin_order_field = 'date'
    formatted_date.short_description = 'Дата та час'