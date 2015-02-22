# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('friends_mapping', '0003_location_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='meeting_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 6, 19, 54, 9, 420000, tzinfo=utc), verbose_name=b'date of the 1st meeting'),
            preserve_default=False,
        ),
    ]
