# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_auto_20160225_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailapross',
            name='work_done',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
