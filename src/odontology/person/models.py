from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Clinic_history(models.Model):
    place = models.CharField(max_length=250)
    date = models.DateField()
    notes = models.CharField(max_length=250)


class Patient(models.Model):
    dentist = models.ForeignKey(User)
    clinic_history = models.OneToOneField(Clinic_history)
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    subsidiary_num = models.PositiveIntegerField(unique=True)
