from __future__ import unicode_literals

from django.db import models
from person.models import Patient


class Fopc(models.Model):
    pass


class Apross(models.Model):
    patient = models.ForeignKey(Patient)
    #--First page
    date = models.DateField(null=True, blank=True)
    managment_code1 = models.IntegerField(null=True, blank=True)
    managment_code2 = models.IntegerField(null=True, blank=True)
    managment_code3 = models.IntegerField(null=True, blank=True)
    rx_amount = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.patient, self.date.month)

    def get_details(self):
        return DetailApross.objects.filter(benefit=self)


class DetailApross(models.Model):
    FACES = (
        (1, 'O/I'), (2, 'L'), (3, 'V'),
        (4, 'P'), (5, 'M'), (6, 'D'),
    )
    detail_id = models.PositiveIntegerField(null=True, blank=True)
    benefit = models.ForeignKey(Apross)
    date = models.DateField(null=True, blank=True)
    work_done = models.CharField(max_length=250, null=True, blank=True)
    practic_code = models.IntegerField(null=True, blank=True)
    element = models.IntegerField(null=True, blank=True)
    faces = models.IntegerField(choices=FACES, null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.benefit, self.detail_id)
