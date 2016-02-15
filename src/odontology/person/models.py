from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Clinic_history(models.Model):
    place = models.CharField(max_length=250)
    date = models.DateField()
    notes = models.CharField(max_length=250)


class Dentist(models.Model):
    user = models.ForeignKey(User)
    circle = models.IntegerField()
    register_number = models.IntegerField()

    class Meta:
        verbose_name = "Odontologo"
        verbose_name_plural = "Odontologos"

    def __unicode__(self):
        return "%s" % (self.user.get_full_name())

GENDER = (
    (1, 'M'),(2, 'F')
)
class Patient(models.Model):
    dentist = models.ForeignKey(Dentist, null=True, blank=True) #sacar el null
    clinic_history = models.OneToOneField(Clinic_history, null=True, blank=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    subsidiary_number = models.PositiveIntegerField("numero de afiliado", unique=True)
    date_created = models.DateField(auto_now_add=True)

    #-- extra info
    incumbent = models.CharField(max_length=250, null=True, blank=True)
    family_group = models.CharField(max_length=250, null=True, blank=True)
    relationship = models.CharField(max_length=250, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    number = models.PositiveIntegerField(null=True, blank=True)
    suburb = models.CharField(max_length=250, null=True, blank=True)
    locality = models.CharField(max_length=250, null=True, blank=True)
    tel = models.IntegerField(null=True, blank=True)
    Workplace_holder = models.CharField(max_length=250, null=True, blank=True)
    hierarchy = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, null=True, blank=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __unicode__(self):
        return "%s %s" % (self.last_name, self.first_name)

    @property
    def domicile(self):
        return self.street + ', ' + str(self.number) + ', ' + self.suburb + ', ' + self.locality

    @property
    def code(self):
        return "P%04d" % (self.id)
