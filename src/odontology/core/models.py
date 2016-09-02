from django.db import models
from django.contrib.auth.models import User


class Day(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.name)


class Bill(models.Model):
    user = models.ForeignKey(User)
    paid = models.BooleanField(default=False)
    linode_file = models.FileField(
        upload_to='linode/', max_length=100, null=True, blank=True
    )
    text = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.user, self.text)


class Chapter(models.Model):
    name = models.CharField(max_length=250)
    number = models.PositiveSmallIntegerField()
    date =  models.DateField('Periodo', null=True, blank=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __unicode__(self):
        return "Chapter %s - %s" % (self.number, self.name.upper())


class Tariff(models.Model):
    chapter = models.ForeignKey(Chapter)
    index = models.PositiveSmallIntegerField(null=True, blank=True)
    sub_index = models.PositiveSmallIntegerField(null=True, blank=True)
    name = models.CharField(blank=True, max_length=250)

    variable_cost = models.DecimalField(
        'Costo variable', max_digits=12, decimal_places=2, default=0
    )
    fixed_cost = models.DecimalField(
        'Costo fijo', max_digits=12, decimal_places=2, default=0
    )
    workshop_cost = models.DecimalField(
        'Costo taller', max_digits=12, decimal_places=2, default=0
    )
    total_cost = models.DecimalField(
        'Costo total', max_digits=12, decimal_places=2, default=0
    )
    fees = models.DecimalField(
        'Honorarios', max_digits=12, decimal_places=2, default=0
    )
    total_tariff = models.DecimalField(
        'Total arancel', max_digits=12, decimal_places=2, default=0
    )

    is_new_code = models.BooleanField(default=False)
    negotiable = models.BooleanField(default=False)

    def get_code(self):
        code =  "%02i" % self.chapter.number
        if self.index:
            code += ".%02i" % self.index
            if self.sub_index:
                code += ".%02i" % self.sub_index
        else:
            code = ''
        return code
