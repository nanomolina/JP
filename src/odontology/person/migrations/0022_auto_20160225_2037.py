# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0021_auto_20160222_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentist',
            name='register_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tel',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
