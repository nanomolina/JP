# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20160217_0155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailapross',
            old_name='date',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='detailapross',
            name='detail_id',
        ),
        migrations.AddField(
            model_name='detailapross',
            name='day',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
