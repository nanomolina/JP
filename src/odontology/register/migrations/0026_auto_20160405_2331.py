# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0025_auto_20160402_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='apross',
            name='observations',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='benefit',
            name='observations',
            field=models.TextField(blank=True, null=True),
        ),
    ]