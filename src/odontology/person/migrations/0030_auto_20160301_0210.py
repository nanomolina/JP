# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0029_auto_20160301_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tooth',
            name='position_x',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tooth',
            name='position_y',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]