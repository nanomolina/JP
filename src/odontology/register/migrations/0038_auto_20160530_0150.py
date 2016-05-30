# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-30 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0037_record_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apross',
            name='real_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='benefit',
            name='real_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='treatment',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
