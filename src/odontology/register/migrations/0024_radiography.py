# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-02 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0023_apross_managment_code4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radiography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.IntegerField(blank=True, choices=[(11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85)], null=True)),
                ('finality', models.IntegerField(blank=True, choices=[(1, 'Diagn\xf3stico'), (2, 'Previa'), (3, 'Conductometr\xeda'), (4, 'Final')], null=True)),
                ('apross', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='register.Apross')),
                ('benefit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='register.Benefit')),
            ],
        ),
    ]
