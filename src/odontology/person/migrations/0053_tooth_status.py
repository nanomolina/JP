# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-29 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0052_auto_20160710_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='tooth',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Rojo'), (2, 'Amarillo'), (3, 'Verde')], default=1),
        ),
    ]
