# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-28 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0028_auto_20160428_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='assistance',
            field=models.SmallIntegerField(choices=[(1, 'Presente'), (2, 'Ausente con aviso'), (3, 'Ausente sin aviso')], default=1),
        ),
        migrations.AlterField(
            model_name='record',
            name='state2',
            field=models.SmallIntegerField(choices=[(1, 'Realizado'), (2, 'Por Terminar'), (3, 'A realizar')], default=3),
        ),
    ]