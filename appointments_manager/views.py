from datetime import datetime
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
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
        for obj in setobj:
            start_str = str(obj.started_at).split('+')[0]
            finish_str = str(obj.finished_at).split('+')[0]
            s = datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S')
            f = datetime.strptime(finish_str, '%Y-%m-%d %H:%M:%S')
            if f.date() == s.date():
                day_string = s.strftime('%Y-%m-%d')
                day.append(day_string)
                time1 = s.strftime('%H:%M')
                time2 = f.strftime('%H:%M')
                time_abs = time1 + '-' + time2
                time.append(time_abs)

        # time_ranges = zip(time, time)
        # date_ranges = zip(day, day)
        # form = VisitorsForm(date_ranges, time_ranges)
        context['date'] = day
        context['time'] = time
        context['form'] = VisitorsForm
        return context

    # def get(self, request, *args, **kwargs):
    #
    #     form = VisitorsForm
    #
    #     return render(request, self.template_name, {'form': form})


class VisitorCreate(SuccessMessageMixin, CreateView):
    model = Visitors
    template_name = "appointment_details.html"
    success_url = reverse_lazy("visitor_new")
    form_class = VisitorsForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form = form.save()

        return HttpResponseRedirect(reverse('appointments'))


class VisitortDetail(DetailView):
    model = Visitors
    template_name = "visitor_details.html"
    success_url = reverse_lazy('appointments')


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