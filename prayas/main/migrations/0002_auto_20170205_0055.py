# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='uploadDate',
            field=models.DateField(default=datetime.date(2017, 2, 5)),
        ),
        migrations.AlterField(
            model_name='students',
            name='joiningDate',
            field=models.DateField(default=datetime.date(2017, 2, 5)),
        ),
        migrations.AlterField(
            model_name='studentsattendancerecord',
            name='date',
            field=models.DateField(default=datetime.date(2017, 2, 5)),
        ),
        migrations.AlterField(
            model_name='volunteerattendancerecord',
            name='date',
            field=models.DateField(default=datetime.date(2017, 2, 5)),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='joiningDate',
            field=models.DateField(default=datetime.date(2017, 2, 5)),
        ),
        migrations.AlterField(
            model_name='volunteerssattendancerecord',
            name='date',
            field=models.DateField(default=datetime.date(2017, 2, 5)),
        ),
    ]
