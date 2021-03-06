# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0015_auto_20160221_2006'),
        ('register', '0011_auto_20160220_0442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('enero', 1), ('febrero', 2), ('marzo', 3), ('abril', 4), ('mayo', 5), ('junio', 6), ('julio', 7), ('agosto', 8), ('septiembre', 9), ('octubre', 10), ('noviembre', 11), ('diciembre', 12)], max_length=15)),
                ('year', models.PositiveIntegerField()),
                ('primary_entity', models.CharField(max_length=250)),
                ('principal_code', models.IntegerField(blank=True, null=True)),
                ('social_worl', models.CharField(blank=True, max_length=250, null=True)),
                ('managment_code', models.IntegerField(blank=True, null=True)),
                ('rx_amount', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('real_date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='DetailBenefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(blank=True, null=True)),
                ('tooth', models.IntegerField(blank=True, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Benefit')),
                ('faces', models.ManyToManyField(blank=True, to='register.Faces')),
            ],
        ),
    ]
