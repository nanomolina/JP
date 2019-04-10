# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-11 05:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20160910_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnualFees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('last_active', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='anual_fees',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AnualFees'),
        ),
    ]