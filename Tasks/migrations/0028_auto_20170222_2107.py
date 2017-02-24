# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 02:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0027_auto_20170222_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createnewdatapullfile',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 2, 7, 51, 45078, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lendingclub_initial_new_origination_data_cleaning',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 2, 7, 51, 46079, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='mergenewcompanydata',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 2, 7, 51, 45578, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='updatingcompanydatastepone',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 2, 7, 51, 44078, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='updatingcompanydatasteptwo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 2, 7, 51, 44578, tzinfo=utc), verbose_name='date published'),
        ),
    ]