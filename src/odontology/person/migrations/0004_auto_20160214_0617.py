# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20160214_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=250),
        ),
    ]