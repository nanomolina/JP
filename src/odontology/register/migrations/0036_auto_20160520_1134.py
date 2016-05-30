# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-20 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0035_auto_20160519_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='assistance',
            field=models.SmallIntegerField(choices=[(1, 'Presente'), (2, 'Ausente con aviso'), (3, 'Ausente sin aviso'), (4, 'Pendiente')], default=1),
        ),
        migrations.AlterField(
            model_name='record',
            name='state',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Realizado'), (2, 'Por Terminar'), (3, 'A realizar')], default=1),
        ),
    ]