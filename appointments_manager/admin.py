from django.contrib import admin
from appointments_manager.models import Appointment, TimeRanges, Visitors, Users

admin.site.register(Appointment)
admin.site.register(Visitors)
admin.site.register(TimeRanges)
admin.site.register(Users)