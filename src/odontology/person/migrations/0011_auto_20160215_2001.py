# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0010_auto_20160215_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='subsidiary_number',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='numero de afiliado'),
        ),
    ]