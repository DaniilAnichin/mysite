# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('friends_mapping', '0007_auto_20150207_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='meeting_date',
            field=models.DateField(verbose_name='date of the 1st meeting', blank=True, default=datetime.datetime(2015, 2, 15, 16, 12, 6, 571200, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='friend',
            field=models.ForeignKey(to='friends_mapping.friend'),
            preserve_default=True,
        ),
    ]
