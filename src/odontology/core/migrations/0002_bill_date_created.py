# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-08 18:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2016, 7, 8, 18, 59, 34, 474240, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
