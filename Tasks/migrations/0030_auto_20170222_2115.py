# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 02:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0029_auto_20170222_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createnewdatapullfile',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 2, 15, 44, 762276, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lendingclub_initial_new_origination_data_cleaning',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 2, 15, 44, 763777, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='mergenewcompanydata',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 2, 15, 44, 762781, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='updatingcompanydatastepone',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 2, 15, 44, 761269, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='updatingcompanydatasteptwo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 2, 15, 44, 761776, tzinfo=utc), verbose_name='date published'),
        ),
    ]
