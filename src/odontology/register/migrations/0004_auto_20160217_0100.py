# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20160216_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apross',
            name='month',
            field=models.CharField(choices=[('enero', 'enero'), ('febrero', 'febrero'), ('marzo', 'marzo'), ('abril', 'abril'), ('mayo', 'mayo'), ('junio', 'junio'), ('julio', 'julio'), ('agosto', 'agosto'), ('septiembre', 'septiembre'), ('octubre', 'octubre'), ('noviembre', 'noviembre'), ('diciembre', 'diciembre')], max_length=15),
        ),
    ]
