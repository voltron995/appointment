from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from appointments_manager.forms import DateForm
from appointments_manager.models import Appointment, TimeRanges, Visitors


class AppointmentList(ListView):
    model = Appointment
    template_name = "appointments.html"
    success_url = reverse_lazy('appointments')

class AppointentCreate(CreateView):
    model = Appointment
    template_name = "appointment_form.html"
    success_url = reverse_lazy('appointments')
    fields = ['name', 'description']

class AppointmentUpdate(UpdateView):
    model = Appointment
    template_name = "appointment_form.html"
    success_url = reverse_lazy('appointments')
    fields = ['name', 'description']

class AppointmentDelete(DeleteView):
    model = Appointment
    template_name = "appointment_confirm_delete.html"
    success_url = reverse_lazy('appointments')

class AppointmentDetail(DetailView):
    model = Appointment
    template_name = "appointment_details.html"
    success_url = reverse_lazy('appointments')

    def get_context_data(self, **kwargs):
        context = super(AppointmentDetail, self).get_context_data(**kwargs)
        context['ranges'] = TimeRanges.objects.filter(appointments_id=self.object.id)
        return context

class VisitorCreate(CreateView):
    model = Visitors
    template_name = "appointment_details.html"
    success_url = reverse_lazy('appointment_details')
    fields = ['full_name', 'email']

class TimeRangesCreate(CreateView):
    model = TimeRanges
    form_class = DateForm
    template_name = "range_form.html"
    success_url = reverse_lazy('appointment_details')

