# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('friends_mapping', '0006_auto_20150207_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='meeting_date',
            field=models.DateField(verbose_name='date of the 1st meeting', default=datetime.datetime(2015, 2, 7, 20, 44, 43, 375600, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='friend',
            field=models.ForeignKey(to='friends_mapping.friend'),
            preserve_default=True,
        ),
    ]
