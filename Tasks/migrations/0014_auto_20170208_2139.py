# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 02:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0013_auto_20170207_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='createnewdatapullfile',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 9, 2, 39, 41, 86201, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='createnewdatapullfile',
            name='QuarterOrAnnual',
            field=models.CharField(choices=[('Annual', 'Annual'), ('Quarterly', 'Quarterly')], default='Annual', max_length=10),
        ),
        migrations.AlterField(
            model_name='updatingcompanydatastepone',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 9, 2, 39, 41, 85700, tzinfo=utc), verbose_name='date published'),
        ),
    ]
