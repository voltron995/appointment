from rest_framework import serializers
from appointments_manager.models import Appointment, TimeRanges, Visitors

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'name', 'description')


class TimeRangesSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer()

    class Meta:
        model = TimeRanges
        fields = ('id', 'started_at', 'finished_at', 'appointments')


class VisitorsSerializer(serializers.ModelSerializer):
    time_ranges = TimeRangesSerializer()

    class Meta:
        model = Visitors
        fields = ('id', 'full_name', 'email', 'time_ranges')