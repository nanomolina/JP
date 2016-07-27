# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-10 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0045_auto_20160510_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='companion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='occupation',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='preferred_day',
            field=models.IntegerField(blank=True, choices=[(1, 'Domingo'), (2, 'Lunes'), (3, 'Martes'), (4, 'Mi\xe9rcoles'), (5, 'Jueves'), (6, 'Viernes'), (7, 'S\xe1bado')], null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='turn',
            field=models.IntegerField(blank=True, choices=[(1, 'Ma\xf1ana'), (2, 'Tarde')], null=True),
        ),
    ]
