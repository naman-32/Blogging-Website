# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-08-26 15:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190825_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 26, 15, 46, 44, 770606, tzinfo=utc)),
        ),
    ]