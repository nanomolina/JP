# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0013_auto_20160216_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='social_work',
            field=models.IntegerField(choices=[(1, 'Ninguna'), (2, 'Apross'), (3, 'Fopc')], default=1),
        ),
    ]
