# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-28 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0030_remove_record_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='state2',
            new_name='state',
        ),
    ]
