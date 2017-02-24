# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 04:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0015_auto_20170208_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createnewdatapullfile',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 9, 4, 23, 22, 606818, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='createnewdatapullfile',
            name='sector',
            field=models.TextField(default='new_tickers', help_text='Annual-10, Quarterly-12'),
        ),
        migrations.AlterField(
            model_name='updatingcompanydatastepone',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 9, 4, 23, 22, 606318, tzinfo=utc), verbose_name='date published'),
        ),
    ]
