# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20160217_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('initial', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='detailapross',
            name='faces',
        ),
        migrations.AddField(
            model_name='detailapross',
            name='faces',
            field=models.ManyToManyField(to='register.Faces'),
        ),
    ]
