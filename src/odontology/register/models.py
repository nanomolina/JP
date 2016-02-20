from __future__ import unicode_literals

from django.db import models
from person.models import Patient


class Fopc(models.Model):
    pass


class Apross(models.Model):
    MONTHS = (
        ('enero', 1), ('febrero', 2), ('marzo', 3), ('abril', 4), ('mayo', 5),
        ('junio', 6), ('julio', 7), ('agosto', 8), ('septiembre', 9),
        ('octubre', 10), ('noviembre', 11), ('diciembre', 12)
    )
    patient = models.ForeignKey(Patient)
    #--First page
    month = models.CharField(choices=MONTHS, max_length=15)
    year = models.PositiveIntegerField()
    managment_code1 = models.IntegerField(null=True, blank=True)
    managment_code2 = models.IntegerField(null=True, blank=True)
    managment_code3 = models.IntegerField(null=True, blank=True)
    rx_amount = models.IntegerField(null=True, blank=True)

    date_created = models.DateField(auto_now_add=True)
    real_date = models.DateField()
    def __unicode__(self):
        return "%s - (%s, %s)" % (self.patient, self.month, self.year)

    def get_details(self):
        return DetailApross.objects.filter(benefit=self)



class DetailApross(models.Model):
    FACES = (
        (1, 'O/I'), (2, 'L'), (3, 'V'),
        (4, 'P'), (5, 'M'), (6, 'D'),
    )
    benefit = models.ForeignKey(Apross)
    day = models.IntegerField(null=True, blank=True)
    work_done = models.CharField(max_length=250, null=True, blank=True)
    practic_code = models.IntegerField(null=True, blank=True)
    element = models.IntegerField(null=True, blank=True)
    faces = models.IntegerField(choices=FACES, null=True, blank=True)
    date_created = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.day, self.benefit)


# DATABASE SIGNALS
from django.db.models.signals import post_save
from django.dispatch import receiver
from register.models import Apross, DetailApross

@receiver(post_save, sender=Apross)
def handler_new_benefit(sender, instance, **kwargs):
    if not instance.get_details().exists():
        for _ in range(4):
            DetailApross(benefit=instance).save()
