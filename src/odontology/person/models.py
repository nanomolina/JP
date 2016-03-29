from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


MONTHS = (
    ('enero', 1), ('febrero', 2), ('marzo', 3), ('abril', 4), ('mayo', 5),
    ('junio', 6), ('julio', 7), ('agosto', 8), ('septiembre', 9),
    ('octubre', 10), ('noviembre', 11), ('diciembre', 12)
)
class Odontogram(models.Model):
    TEETH_NUMBERS = tuple([(x, x) for x in range(33)])
    teeth_number = models.SmallIntegerField(choices=TEETH_NUMBERS, null=True, blank=True)
    observations = models.TextField(null=True, blank=True)
    month = models.CharField(choices=MONTHS, max_length=15, null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % str(self.id)

    def get_teeth(self):
        return Tooth.objects.filter(odontogram=self)

    def period(self):
        if self.month is not None and self.year is not None:
            result = str(self.month) + ' - ' + str(self.year)
        else:
            result = '-'
        return result


class Clinic_history(models.Model):
    place = models.CharField(max_length=250)
    date = models.DateField()
    notes = models.CharField(max_length=250)


class SocialWork(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    initial = models.CharField(max_length=250)

    def __unicode__(self):
        return "%s" % (self.initial)


class Dentist(models.Model):
    user = models.ForeignKey(User)
    circle = models.CharField(max_length=15, null=True, blank=True)
    register_number = models.CharField(max_length=25, null=True, blank=True)
    carrying_home = models.CharField(max_length=250, null=True, blank=True)

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
    subsidiary_number = models.CharField(
        "numero de afiliado", max_length=25, null=True, blank=True
    )
    date_created = models.DateField(auto_now_add=True)
    social_work = models.ForeignKey(SocialWork, null=True, blank=True)
    odontogram = models.ForeignKey(Odontogram, null=True, blank=True)

    #-- extra info
    incumbent = models.CharField(max_length=250, null=True, blank=True)
    family_group = models.CharField(max_length=250, null=True, blank=True)
    relationship = models.CharField(max_length=250, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    number = models.PositiveIntegerField(null=True, blank=True)
    floor = models.CharField(max_length=5, null=True, blank=True)
    apartment = models.CharField(max_length=5, null=True, blank=True)
    neighborhood = models.CharField(max_length=250, null=True, blank=True)
    suburb = models.CharField(max_length=250, null=True, blank=True)
    locality = models.CharField(max_length=250, null=True, blank=True)
    tel = models.CharField(max_length=250, null=True, blank=True)
    Workplace_holder = models.CharField(max_length=250, null=True, blank=True)
    hierarchy = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, null=True, blank=True)
    derivation = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def domicile(self):
        result = ''
        if self.street not in [None, '']:
            result += self.street
        if self.number not in [None, '']:
            result += ' ' + str(self.number)
        if self.floor not in [None, '']:
            result += ', dpto ' + self.floor
        if self.apartment not in [None, '']:
            result += ' ' + self.apartment
        if self.neighborhood not in [None, '']:
            result += '. Barrio ' + self.neighborhood
        return result

    @property
    def full_locality(self):
        if self.suburb not in [None, '']:
            if self.locality not in [None, '']:
                result = self.suburb + ', ' + self.locality
            else:
                result = self.suburb
        else:
            result = None
        return result

    @property
    def code(self):
        return "P%04d" % (self.id)

    def get_full_name(self):
        return "%s %s" % (self.last_name, self.first_name)

    def get_benefits(self):
        from register.models import Apross, Benefit
        if self.social_work and self.social_work.initial == 'APROSS':
            benefit = Apross.objects.filter(patient=self)
        else:
            benefit = Benefit.objects.filter(patient=self)
        return benefit

COLORS = ((1, 'red'), (2, 'blue'))
WORK_TYPES = (
    (1, 'Extraccion'), (2, 'Endodoncia'), (3, 'Restauracion'),
    (4, 'Restauracion filtrada'), (5, 'Caries'), (6, 'Corona')
)
POS_X1 = tuple([(x , x*25) for x in range(8)])
POS_X_2 = tuple([(x+8 , 210+x*25) for x in range(8)])
POS_X = POS_X1 + POS_X_2
POS_Y = tuple([(y, y*40) for y in range(4)])
class Tooth(models.Model):
    from register.models import ELEMENTS

    odontogram = models.ForeignKey(Odontogram)
    number = models.SmallIntegerField(choices=ELEMENTS)
    color = models.SmallIntegerField(choices=COLORS, null=True, blank=True)
    work_type = models.SmallIntegerField(choices=WORK_TYPES, null=True, blank=True)
    position_x = models.SmallIntegerField(null=True, blank=True)
    position_y = models.SmallIntegerField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % str(self.number)

    def get_sectors(self):
        return Sector.objects.filter(tooth=self)


LOCATIONS = (
    (1, 'C'), (2, 'T'), (3, 'B'), (4, 'R'), (5, 'L')
)
class Sector(models.Model):
    POINTS = (
        (1, '5,5    15,5    15,15   5,15'),
        (2, '0,0    20,0    15,5    5,5'),
        (3, '5,15   15,15   20,20   0,20'),
        (4, '15,5   20,0    20,20   15,15'),
        (5, '0,0    5,5     5,15    0,20')
    )
    tooth = models.ForeignKey(Tooth)
    location = models.SmallIntegerField(choices=LOCATIONS)
    color = models.SmallIntegerField(choices=COLORS, null=True, blank=True)
    points = models.SmallIntegerField(choices=POINTS, null=True, blank=True)
    stroke_blue = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s" % str(self.location)
