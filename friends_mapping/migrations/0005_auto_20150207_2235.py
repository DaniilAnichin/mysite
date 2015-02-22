# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('friends_mapping', '0004_friend_meeting_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='meeting_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 7, 20, 35, 27, 95600, tzinfo=utc), blank=True, verbose_name='date of the 1st meeting'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='arrivals_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 7, 20, 35, 27, 96600, tzinfo=utc), blank=True, verbose_name='date arrived'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='departure_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 7, 20, 35, 27, 96600, tzinfo=utc), blank=True, verbose_name='date departured'),
            preserve_default=True,
        ),
    ]
