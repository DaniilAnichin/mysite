# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends_mapping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='friend',
            field=models.ForeignKey(to='friends_mapping.friend'),
            preserve_default=True,
        ),
    ]
