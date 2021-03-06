    # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from person.models import Patient
from core.models import Tariff


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
    rx_amount = models.IntegerField(null=True, blank=True) #no se usa
    observations = models.TextField(null=True, blank=True)
    printed = models.BooleanField(default=False)

    date_created = models.DateField(auto_now_add=True)
    real_date = models.DateField(null=True)
    def __unicode__(self):
        return "%s - (%s, %s)" % (self.patient, self.month, self.year)

    def get_details(self):
        return DetailApross.objects.filter(benefit=self).order_by('id')

    def get_elements(self):
        return DetailApross.objects.filter(benefit=self).values_list('element', flat=True)

    def get_empty_detail(self):
        for detail in self.get_details():
            if detail.is_empty():
                return detail
        return None


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

    def is_empty(self):
        return self.day is None and self.work_done in [None, ''] and \
            self.practic_code in [None, ''] and self.element is None and \
            self.faces.count() == 0


class Benefit(models.Model):
    patient = models.ForeignKey(Patient)
    #--First page
    month = models.CharField(choices=MONTHS, max_length=15)
    year = models.PositiveIntegerField()
    primary_entity = models.CharField(max_length=250, null=True, blank=True)
    principal_code = models.IntegerField(null=True, blank=True)
    social_work = models.CharField(max_length=250, null=True, blank=True)
    managment_code = models.CharField(max_length=15, null=True, blank=True)
    rx_amount = models.IntegerField(null=True, blank=True) #no se usa
    observations = models.TextField(null=True, blank=True)
    printed = models.BooleanField(default=False)

    date_created = models.DateField(auto_now_add=True)
    real_date = models.DateField(null=True)
    def __unicode__(self):
        return "%s - (%s, %s)" % (self.patient, self.month, self.year)

    def get_details(self):
        return DetailBenefit.objects.filter(benefit=self).order_by('id')

    def get_elements(self):
        return DetailBenefit.objects.filter(benefit=self).values_list('tooth', flat=True)

    def get_empty_detail(self):
        for detail in self.get_details():
            if detail.is_empty():
                return detail
        return None


class DetailBenefit(models.Model):
    benefit = models.ForeignKey(Benefit)
    day = models.IntegerField(null=True, blank=True)
    tooth = models.IntegerField(choices=ELEMENTS, null=True, blank=True)
    code = models.CharField(max_length=15, null=True, blank=True)
    faces = models.ManyToManyField(Faces, blank=True)
    date_created = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.day, self.benefit)

    def is_empty(self):
        return self.day is None and self.tooth is None and \
            self.faces.count() == 0 and self.code in [None, '']


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

    @property
    def rx_amount(self):
        count = 0
        if self.part_number_1 is not None and self.finality_1 is not None:
            count += 1
        if self.part_number_2 is not None and self.finality_2 is not None:
            count += 1
        if self.part_number_3 is not None and self.finality_3 is not None:
            count += 1
        return count


class Record(models.Model):
    STATES = (
        (1, 'Realizado'), (2, 'Por Terminar'), (3, 'A realizar')
    )
    ASSISTANCE = (
        (1, 'Presente'), (2, 'Ausente con aviso'), (3, 'Ausente sin aviso'), (4, 'Pendiente'),
    )
    patient = models.ForeignKey(Patient)
    date = models.DateTimeField(null=True, blank=True)
    treatment = models.CharField(max_length=250 ,null=True, blank=True)
    faces = models.ManyToManyField(Faces, blank=True)
    tooth = models.IntegerField(choices=ELEMENTS, null=True, blank=True)
    period_so = models.CharField(max_length=30, null=True, blank=True)
    state = models.SmallIntegerField(choices=STATES, default=1, blank=True)
    assistance = models.SmallIntegerField(choices=ASSISTANCE, default=1)
    observations = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=15, null=True, blank=True)
    tariff = models.ForeignKey(Tariff, null=True, blank=True)
    to_account = models.BooleanField(default=True)
    to_social_work = models.BooleanField(default=True)

    #Accounting
    debit = models.DecimalField(
        max_digits=7, decimal_places=0, default=0,
    )
    havings = models.DecimalField(
        max_digits=7, decimal_places=0, default=0,
    )
    # other
    date_created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % (self.patient)

    @property
    def balance(self):
        return self.debit - self.havings

    def create_social_work(self):
        try:
            month, year = self.period_so.split(' - ')
        except ValueError:
            return None
        if self.patient.social_work and self.patient.social_work.initial == 'APROSS':
            benefit, created = Apross.objects.get_or_create(
                patient=self.patient, month=month, year=int(year)
            )
            if created:
                from datetime import date as Date
                benefit.real_date = Date(int(year), int(benefit.get_month_display()), 1)
                benefit.save()
            new_detail = benefit.get_empty_detail()
            if new_detail is not None:
                new_detail.work_done = self.treatment
                new_detail.practic_code = self.code
                new_detail.element = self.tooth
                for face in self.faces.all():
                    new_detail.faces.add(face)
                new_detail.save()
        else:
            benefit, created = Benefit.objects.get_or_create(
                patient=self.patient, month=month, year=int(year)
            )
            if created:
                from datetime import date as Date
                benefit.real_date = Date(int(year), int(benefit.get_month_display()), 1)
                benefit.save()
            new_detail = benefit.get_empty_detail()
            if new_detail is not None:
                new_detail.code = self.code
                new_detail.tooth = self.tooth
                for face in self.faces.all():
                    new_detail.faces.add(face)
                new_detail.save()


class CurrentAccount(models.Model):
    patient = models.ForeignKey(Patient)
    date = models.DateTimeField(null=True, blank=True)
    record = models.ForeignKey(Record, null=True, blank=True)
    debit = models.DecimalField(
        max_digits=7, decimal_places=0, default=0,
    )
    havings = models.DecimalField(
        max_digits=7, decimal_places=0, default=0,
    )

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __unicode__(self):
        return "%s" % (self.patient)

    @property
    def balance(self):
        return self.debit - self.havings


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
