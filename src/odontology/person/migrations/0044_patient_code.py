# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-10 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0043_auto_20160510_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]