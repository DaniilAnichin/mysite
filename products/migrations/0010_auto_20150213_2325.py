# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20150213_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='id',
            new_name='obj_id',
        ),
    ]
