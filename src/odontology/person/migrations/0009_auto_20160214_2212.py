# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('person', '0008_patient_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dentist',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='dentist',
            name='last_name',
        ),
        migrations.AddField(
            model_name='dentist',
            name='user',
            field=models.ForeignKey(default=12, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
