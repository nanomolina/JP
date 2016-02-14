from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Clinic_history(models.Model):
    place = models.CharField(max_length=250)
    date = models.DateField()
    notes = models.CharField(max_length=250)


class Dentist(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    circle = models.IntegerField()
    register_number = models.IntegerField()


class Patient(models.Model):
    dentist = models.ForeignKey(Dentist, null=True, blank=True) #sacar el null
    clinic_history = models.OneToOneField(Clinic_history, null=True, blank=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    subsidiary_number = models.PositiveIntegerField("numero de afiliado", unique=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
