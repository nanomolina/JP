# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_benefit_detailbenefit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benefit',
            old_name='social_worl',
            new_name='social_work',
        ),
        migrations.AlterField(
            model_name='benefit',
            name='primary_entity',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
