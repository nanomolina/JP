# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-24 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0036_auto_20160520_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='code',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
