# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0026_auto_20160228_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='apartment',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='floor',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]