# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0014_auto_20160216_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='subsidiary_number',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True, verbose_name='numero de afiliado'),
        ),
    ]