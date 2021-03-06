# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-13 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='memory_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minion_id', models.CharField(max_length=20)),
                ('memory_total', models.IntegerField(default=0)),
                ('memory_used', models.IntegerField(default=0)),
                ('memory_free', models.IntegerField(default=0)),
                ('memory_share', models.IntegerField(default=0)),
                ('memory_bu_ca', models.IntegerField(default=0)),
                ('memory_available', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='monitor_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitor_name', models.CharField(max_length=20)),
                ('monitor_type', models.IntegerField(default=0)),
                ('monitor_description', models.CharField(max_length=50)),
            ],
        ),
    ]
