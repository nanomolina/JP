# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0039_auto_20160419_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]