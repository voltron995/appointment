from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import generics
from appointments_manager.forms import VisitorsForm, DateForm
from appointments_manager.models import Appointment, TimeRanges, Visitors
from appointments_manager.serializers import AppointmentSerializer

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
    form_class = VisitorsForm
    template_name = "appointment_details.html"
    success_url = reverse_lazy('appointments')

    def get_context_data(self, **kwargs):
        context = super(AppointmentDetail, self).get_context_data(**kwargs)
        setobj = TimeRanges.objects.filter(appointments_id=self.object.id)
        day = []
        time = []
        current_id = 0
        for obj in setobj:
            start_str = str(obj.started_at).split('+')[0]
            finish_str = str(obj.finished_at).split('+')[0]
            s = datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S')
            f = datetime.strptime(finish_str, '%Y-%m-%d %H:%M:%S')
            if f.date() == s.date():
                current_id += 1
                day_string = s.strftime('%Y-%m-%d')
                date_dict = {'id': obj.id, 'value': day_string}
                day.append(date_dict)
                time1 = s.strftime('%H:%M')
                time2 = f.strftime('%H:%M')
                time_abs = time1 + '-' + time2
                time_dict = {'id': current_id, 'date_id': obj.id, 'value': time_abs}
                time.append(time_dict)

        time_ranges = setobj
        context['date'] = day
        context['time'] = time
        context['form'] = VisitorsForm(time_ranges)
        return context


class VisitorCreate(CreateView):
    model = Visitors
    template_name = "appointment_details.html"
    form_class = VisitorsForm
    success_url = reverse_lazy('appointments')

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(kwargs, request.POST)
    #     print(request.POST)
    #     if form.is_valid():
    #         print('*********')
    #         form = form.save()
    #
    #     return render(request, self.success_url, {'form': form})


class VisitortDetail(DetailView):
    model = Visitors
    template_name = "visitor_details.html"
    success_url = reverse_lazy('appointments')


class VisitorFilledFormsList(LoginRequiredMixin, ListView):
    model = Visitors
    template_name = "visitor_filled_forms.html"
    success_url = reverse_lazy('appointments')

    def get_context_data(self, *args, **kwargs):
        context = super(VisitorFilledFormsList, self).get_context_data(**kwargs)
        context['object_list'] = self.object_list.filter(appointments=self.kwargs['pk'])
        return context

class TimeRangesCreate(CreateView):
    model = TimeRanges
    form_class = DateForm
    template_name = "range_form.html"
    success_url = reverse_lazy('appointments')


class AppList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer