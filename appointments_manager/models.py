from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())

    class Meta:
        abstract = True

class Appointment(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('appointment', kwargs={'pk': self.pk})

class TimeRanges(BaseModel):
    started_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    finished_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    appointments = models.ForeignKey(Appointment)

    def get_absolute_url(self):
        return reverse('time_range', kwargs={'pk': self.pk})


class Visitors(BaseModel):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    time_ranges = models.ForeignKey(TimeRanges)
    appointments = models.ForeignKey(Appointment)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('visitor', kwargs={'pk': self.pk})

