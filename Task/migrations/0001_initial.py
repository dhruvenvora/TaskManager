# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 00:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('taskid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('creation_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('due_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('is_rotation', models.BooleanField(default=0)),
                ('remind_before', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('duration', models.DurationField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
