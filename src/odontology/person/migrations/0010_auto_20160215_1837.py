# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_auto_20160214_2212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dentist',
            options={'verbose_name': 'Odontologo', 'verbose_name_plural': 'Odontologos'},
        ),
        migrations.AddField(
            model_name='patient',
            name='benefit_type',
            field=models.IntegerField(default=1, choices=[(1, 'Apross'), (2, 'Fopc')]),
            preserve_default=False,
        ),
    ]
