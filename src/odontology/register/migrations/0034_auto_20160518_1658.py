# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-18 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0033_auto_20160513_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='debit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='record',
            name='havings',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]