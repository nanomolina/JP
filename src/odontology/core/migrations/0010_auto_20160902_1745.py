# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-02 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_chapter_tariff'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='is_new_code',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tariff',
            name='negotiable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name=b'Periodo'),
        ),
    ]
