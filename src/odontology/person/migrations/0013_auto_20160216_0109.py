# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 04:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0012_dentist_carrying_home'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='benefit_type',
            new_name='social_work',
        ),
    ]
