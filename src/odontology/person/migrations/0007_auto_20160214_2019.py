# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_remove_patient_reciently_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Workplace_holder',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='family_group',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'M'), (2, 'F')]),
        ),
        migrations.AddField(
            model_name='patient',
            name='hierarchy',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='incumbent',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='locality',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='number',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='relationship',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='street',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='suburb',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='tel',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
