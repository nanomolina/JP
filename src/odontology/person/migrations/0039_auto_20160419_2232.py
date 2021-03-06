# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-20 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0038_patient_cel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentist',
            name='carrying_home',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Domicilio'),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='circle',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='C\xedrculo'),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='register_number',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Registro'),
        ),
    ]
