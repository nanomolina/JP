# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0017_delete_socialwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('initial', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='social_work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='person.SocialWork'),
        ),
    ]