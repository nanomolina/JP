# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-10 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0047_auto_20160710_0347'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PreferredDay',
        ),
        migrations.AlterField(
            model_name='patient',
            name='preferred_day',
            field=models.ManyToManyField(blank=True, to='core.Day'),
        ),
    ]
