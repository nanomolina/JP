# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 02:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0012_dentist_carrying_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apross',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('managment_code1', models.IntegerField(blank=True, null=True)),
                ('managment_code2', models.IntegerField(blank=True, null=True)),
                ('managment_code3', models.IntegerField(blank=True, null=True)),
                ('rx_amount', models.IntegerField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='detailApross',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_id', models.PositiveIntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('work_done', models.CharField(max_length=250)),
                ('practic_code', models.IntegerField(blank=True, null=True)),
                ('element', models.IntegerField(blank=True, null=True)),
                ('faces', models.IntegerField(blank=True, choices=[(1, 'O/I'), (2, 'L'), (3, 'V'), (4, 'P'), (5, 'M'), (6, 'D')], null=True)),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Apross')),
            ],
        ),
        migrations.CreateModel(
            name='Fopc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
