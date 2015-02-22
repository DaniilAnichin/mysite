# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('friends_mapping', '0005_auto_20150207_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='meeting_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 7, 20, 39, 20, 242600, tzinfo=utc), verbose_name='date of the 1st meeting', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='arrivals_date',
            field=models.DateField(null=True, verbose_name='date arrived'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='departure_date',
            field=models.DateField(null=True, verbose_name='date departured'),
            preserve_default=True,
        ),
    ]
