from django.urls import path

from .views import (
    ReminderListView, ReminderDetailView,
    ReminderCreateView, ReminderUpdateView, ReminderDeleteView,
    home
)

urlpatterns = [
    path('list/', ReminderListView.as_view(), name='reminder_list'),
    path('<int:pk>/', ReminderDetailView.as_view(), name='reminder_detail'),
    path('add/', ReminderCreateView.as_view(), name='reminder_add'),
    path('<int:pk>/edit/', ReminderUpdateView.as_view(), name='reminder_edit'),
    path('<int:pk>/delete/', ReminderDeleteView.as_view(), name='reminder_delete'),
    path('', home, name='home'),
]
