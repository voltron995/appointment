from bootstrap3_datetime import widgets
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

from appointments_manager.models import TimeRanges, Visitors, Appointment

class DateForm(forms.ModelForm):

    class Meta:
        model = TimeRanges
        fields = ['started_at', 'finished_at', 'appointments']


        started_at = forms.DateTimeField(required=False,  localize=True, input_formats=['%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
                                                                                         '%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
                                                                                         '%Y-%m-%d',             # '2006-10-25'
                                                                                         '%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
                                                                                         '%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
                                                                                         '%m/%d/%Y',             # '10/25/2006'
                                                                                         '%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
                                                                                         '%m/%d/%y %H:%M',       # '10/25/06 14:30'
                                                                                         '%m/%d/%y']),
        finished_at = forms.DateTimeField(required=False, localize=True, input_formats=['%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
                                                                                         '%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
                                                                                         '%Y-%m-%d',             # '2006-10-25'
                                                                                         '%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
                                                                                         '%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
                                                                                         '%m/%d/%Y',             # '10/25/2006'
                                                                                         '%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
                                                                                         '%m/%d/%y %H:%M',       # '10/25/06 14:30'
                                                                                         '%m/%d/%y']),
        appointments = forms.ChoiceField(choices=Appointment.objects.all())

class VisitorsForm(forms.ModelForm):
    class Meta:
        model = Visitors
        fields = ['full_name', 'time_ranges', 'email', 'appointments']
    full_name = forms.CharField(required=True, widget=forms.TextInput),
    email = forms.EmailField(required=True, widget=forms.EmailInput),

    def __init__(self, time_ranges, appointments, *args, **kwargs):
        super(VisitorsForm, self).__init__(*args, **kwargs)
        self.fields['time_ranges'].choises = time_ranges
        self.fields['appointments'].choises = appointments


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'description']

    name = forms.CharField(required=True, widget=forms.TextInput),
    description = forms.CharField(widget=forms.Textarea)


