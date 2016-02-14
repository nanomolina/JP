from __future__ import unicode_literals

from django.db import models
from person.models import Patient


class Fopc(models.Model):
    pass


class Apross(models.Model):
    patient = models.ForeignKey(Patient)
