# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-21 12:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2017, 1, 21, 12, 37, 29, 152579, tzinfo=utc)),
        ),
    ]
