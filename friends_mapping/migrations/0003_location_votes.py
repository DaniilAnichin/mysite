# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends_mapping', '0002_auto_20150206_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
