# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0022_auto_20160310_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='apross',
            name='managment_code4',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
