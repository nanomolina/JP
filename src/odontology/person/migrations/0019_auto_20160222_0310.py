# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0018_auto_20160222_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialwork',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]