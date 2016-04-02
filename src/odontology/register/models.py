# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from person.models import Patient


class Fopc(models.Model):
    pass


class Faces(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    initial = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Cara'
        verbose_name_plural = 'Caras'

    def __unicode__(self):
        return "%s" % (self.initial)


MONTHS = (
    ('enero', 1), ('febrero', 2), ('marzo', 3), ('abril', 4), ('mayo', 5),
    ('junio', 6), ('julio', 7), ('agosto', 8), ('septiembre', 9),
    ('octubre', 10), ('noviembre', 11), ('diciembre', 12)
)
class Apross(models.Model):
    patient = models.ForeignKey(Patient)
    #--First page
    month = models.CharField(choices=MONTHS, max_length=15)
    year = models.PositiveIntegerField()
    managment_code1 = models.CharField(max_length=15, null=True, blank=True)
    managment_code2 = models.CharField(max_length=15, null=True, blank=True)
    managment_code3 = models.CharField(max_length=15, null=True, blank=True)
    managment_code4 = models.CharField(max_length=15, null=True, blank=True)
    rx_amount = models.IntegerField(null=True, blank=True)

    date_created = models.DateField(auto_now_add=True)
    real_date = models.DateField()
    def __unicode__(self):
        return "%s - (%s, %s)" % (self.patient, self.month, self.year)

    def get_details(self):
        return DetailApross.objects.filter(benefit=self).order_by('id')


milk_teeth = range(51, 56) + range(61,66) + range(71,76) + range(81, 86)
MILK_TEETH = tuple([(x, x) for x in milk_teeth])
list_elements = range(11,19) + range(21,29) + range(31,39) + range(41,49) + milk_teeth
ELEMENTS = tuple([(x, x) for x in list_elements])
class DetailApross(models.Model):
    benefit = models.ForeignKey(Apross)
    day = models.IntegerField(null=True, blank=True)
    work_done = models.CharField(max_length=250, null=True, blank=True)
    practic_code = models.CharField(max_length=15, null=True, blank=True)
    element = models.IntegerField(choices=ELEMENTS, null=True, blank=True)
    date_created = models.DateField(null=True, blank=True)
    faces = models.ManyToManyField(Faces, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.day, self.benefit)


class Benefit(models.Model):
    patient = models.ForeignKey(Patient)
    #--First page
    month = models.CharField(choices=MONTHS, max_length=15)
    year = models.PositiveIntegerField()
    primary_entity = models.CharField(max_length=250, null=True, blank=True)
    principal_code = models.IntegerField(null=True, blank=True)
    social_work = models.CharField(max_length=250, null=True, blank=True)
    managment_code = models.CharField(max_length=15, null=True, blank=True)
    rx_amount = models.IntegerField(null=True, blank=True)

    date_created = models.DateField(auto_now_add=True)
    real_date = models.DateField()
    def __unicode__(self):
        return "%s - (%s, %s)" % (self.patient, self.month, self.year)

    def get_details(self):
        return DetailBenefit.objects.filter(benefit=self).order_by('id')


class DetailBenefit(models.Model):
    benefit = models.ForeignKey(Benefit)
    day = models.IntegerField(null=True, blank=True)
    tooth = models.IntegerField(choices=ELEMENTS, null=True, blank=True)
    code = models.CharField(max_length=15, null=True, blank=True)
    faces = models.ManyToManyField(Faces, blank=True)
    date_created = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.day, self.benefit)


class Radiography(models.Model):
    FINALITYS = (
        (1, 'Diagnóstico'), (2, 'Previa'), (3, 'Conductometría'), (4, 'Final')
    )
    apross = models.ForeignKey(Apross, null=True, blank=True)
    benefit = models.ForeignKey(Benefit, null=True, blank=True)

    part_number_1 = models.IntegerField(choices=ELEMENTS, null=True, blank=True)
    finality_1 = models.IntegerField(choices=FINALITYS, null=True, blank=True)
    part_number_2 = models.IntegerField(choices=ELEMENTS, null=True, blank=True)
    finality_2 = models.IntegerField(choices=FINALITYS, null=True, blank=True)
    part_number_3 = models.IntegerField(choices=ELEMENTS, null=True, blank=True)
    finality_3 = models.IntegerField(choices=FINALITYS, null=True, blank=True)

    def __unicode__(self):
        if self.apross:
            return "%s" % (self.apross.patient)
        elif self.benefit:
            return "%s" % (self.benefit.patient)
        else:
            return "None"


# DATABASE SIGNALS
from django.db.models.signals import post_save
from django.dispatch import receiver
from register.models import Apross, DetailApross, Benefit, DetailBenefit

@receiver(post_save, sender=Apross)
def handler_new_apross(sender, instance, **kwargs):
    if not instance.get_details().exists():
        for _ in range(4):
            DetailApross(benefit=instance).save()
        Radiography(apross=instance).save()


@receiver(post_save, sender=Benefit)
def handler_new_benefit(sender, instance, **kwargs):
    if not instance.get_details().exists():
        for _ in range(4):
            DetailBenefit(benefit=instance).save()
        Radiography(benefit=instance).save()
