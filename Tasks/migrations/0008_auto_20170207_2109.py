# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 02:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0007_auto_20170206_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatingcompanydatastepone',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 8, 2, 9, 49, 572739, tzinfo=utc), verbose_name='date published'),
        ),
    ]
