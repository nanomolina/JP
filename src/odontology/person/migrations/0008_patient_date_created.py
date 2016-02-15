# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0007_auto_20160214_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2016, 2, 15, 1, 6, 14, 723509, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
