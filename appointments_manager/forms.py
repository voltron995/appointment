from bootstrap3_datetime import widgets
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

from appointments_manager.models import TimeRanges, Visitors

class DateForm(forms.ModelForm):

    class Meta:
        model = TimeRanges
        fields = ['started_at', 'finished_at']

        widgets = {
            'started_at': forms.DateInput(attrs={'class' : 'datetimepicker'}),
            'finished_at': forms.DateInput(attrs={'class' : 'datetimepicker'}),
        }

class VisitorsForm(forms.ModelForm):
    class Meta:
        model = Visitors
        fields = ['full_name', 'time_ranges', 'email']
        exclude = ['appointments']
    full_name = forms.CharField(required=True, widget=forms.TextInput),
    email = forms.EmailField(required=True, widget=forms.EmailInput),

    def __init__(self, time_ranges, *args, **kwargs):
        super(VisitorsForm, self).__init__(*args, **kwargs)
        self.fields['time_ranges'].choises = time_ranges



# class VisitorsForm(forms.Form):
    # date = forms.ChoiceField(widget=forms.RadioSelect)
    # time = forms.ChoiceField(widget=forms.RadioSelect)
    # contact_name = forms.CharField(required=True, widget=forms.TextInput)
    # contact_email = forms.EmailField(required=True, widget=forms.EmailInput)
    # time_ranges = forms.IntegerField(widget=forms.HiddenInput(), initial=1)

    # def __init__(self, date_ranges, time_ranges, *args, **kwargs):
    #     super(VisitorsForm, self).__init__(*args, **kwargs)
    #     self.fields['time'].choices = time_ranges
    #     self.fields['date'].choices = date_ranges