from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
# Create your models here.

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())

    class Meta:
        abstract = True

class TimeRanges(BaseModel):
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('time_range', kwargs={'pk': self.pk})

class Appointment(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    time_ranges = models.ManyToManyField(TimeRanges)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('appointment', kwargs={'pk': self.pk})



class Visitors(BaseModel):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    time_ranges = models.ForeignKey(TimeRanges)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('visitor', kwargs={'pk': self.pk})

class Users(BaseModel):
    login = models.CharField(unique=True, max_length=100)
    password_hash = models.CharField(unique=True, max_length=200)
    is_registered = models.BooleanField(default=False)
    appointments = models.ManyToManyField(Appointment)

    def __str__(self):
        return self.login

    def get_absolute_url(self):
        return reverse('user', kwargs={'pk': self.pk})
