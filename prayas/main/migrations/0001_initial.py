# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='mainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('ourMotto', models.CharField(max_length=400)),
                ('videoLink', models.CharField(max_length=300)),
                ('volunteer1', models.CharField(max_length=20)),
                ('volunteer2', models.CharField(max_length=20)),
                ('volunteer3', models.CharField(max_length=20)),
                ('volunteer4', models.CharField(max_length=20)),
                ('volunteer5', models.CharField(max_length=20)),
                ('student1', models.CharField(max_length=20)),
                ('student2', models.CharField(max_length=20)),
                ('student3', models.CharField(max_length=20)),
                ('student5', models.CharField(max_length=20)),
                ('student4', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='notices',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('uploadDate', models.DateField(default=datetime.date(2017, 2, 3))),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='photoGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('year', models.IntegerField()),
                ('event', models.ForeignKey(to='main.events')),
            ],
        ),
        migrations.CreateModel(
            name='studentPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('year', models.IntegerField()),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('rollNo', models.CharField(serialize=False, max_length=20, primary_key=True)),
                ('address', models.CharField(max_length=200)),
                ('isActive', models.BooleanField(default=True)),
                ('guardianName', models.CharField(max_length=50)),
                ('guardianPhone', models.CharField(max_length=10)),
                ('guardiansRelationWithChild', models.CharField(max_length=20)),
                ('referenceName', models.CharField(max_length=50)),
                ('referencePhone', models.CharField(max_length=10)),
                ('referenceAddress', models.CharField(max_length=200)),
                ('joiningDate', models.DateField(default=datetime.date(2017, 2, 3))),
            ],
        ),
        migrations.CreateModel(
            name='studentsAttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(default=datetime.date(2017, 2, 3))),
                ('present', models.BooleanField(default=True)),
                ('student', models.ForeignKey(to='main.students')),
            ],
        ),
        migrations.CreateModel(
            name='volunteerAttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(default=datetime.date(2017, 2, 3))),
            ],
        ),
        migrations.CreateModel(
            name='volunteers',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('collegeRollNo', models.CharField(serialize=False, max_length=10, primary_key=True)),
                ('joiningDate', models.DateField(default=datetime.date(2017, 2, 3))),
                ('email', models.EmailField(max_length=254)),
                ('contactNo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='volunteerssAttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(default=datetime.date(2017, 2, 3))),
                ('present', models.BooleanField(default=True)),
                ('volunteer', models.ForeignKey(to='main.volunteers')),
            ],
        ),
        migrations.AddField(
            model_name='volunteerattendancerecord',
            name='volunteer',
            field=models.ForeignKey(to='main.volunteers'),
        ),
        migrations.AddField(
            model_name='studentperformance',
            name='student',
            field=models.ForeignKey(to='main.students'),
        ),
    ]
