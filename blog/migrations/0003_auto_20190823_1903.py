# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-08-23 13:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190823_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 23, 13, 33, 43, 277470, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 23, 13, 33, 43, 272469, tzinfo=utc)),
        ),
    ]
