from bootstrap3_datetime import widgets
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

from appointments_manager.models import TimeRanges

class DateForm(forms.ModelForm):

    class Meta:
        model = TimeRanges
        fields = ['started_at', 'finished_at']

        widgets = {
            'started_at': forms.DateInput(attrs={'class' : 'datepicker'}),
        }


    #
    # todo = forms.CharField(
    #     widget=forms.TextInput(attrs={"class": "form-control"}))
    # date = forms.DateField(
    #     widget=DateTimePicker(options={"format": "YYYY-MM-DD",
    #                                    "pickTime": False}))
    # reminder = forms.DateTimeField(
    #     required=False,
    #     widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
    #                                    "pickSeconds": False}))