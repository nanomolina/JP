# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-02 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0037_auto_20160328_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='cel_phone',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
