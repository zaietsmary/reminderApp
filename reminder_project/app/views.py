from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Reminder
from .forms import ReminderForm
from django.core.exceptions import ObjectDoesNotExist
from .tasks import send_reminder

class ReminderListView(ListView):
    model = Reminder
    template_name = 'reminder_list.html'
    context_object_name = 'reminders'

class ReminderDetailView(DetailView):
    model = Reminder
    template_name = 'reminder_detail.html'
    context_object_name = 'reminder'

class ReminderCreateView(CreateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'reminder_form.html'
    success_url = reverse_lazy('reminder_list')

    def form_valid(self, form):
        reminder = form.save()
        send_reminder.apply_async(args=[reminder.id], eta=reminder.date)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        return context

class ReminderUpdateView(UpdateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'reminder_form.html'
    success_url = reverse_lazy('reminder_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        return context

class ReminderDeleteView(DeleteView):
    model = Reminder
    template_name = 'reminder_confirm_delete.html'
    success_url = reverse_lazy('reminder_list')

