# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20150213_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='obj_id',
            new_name='id',
        ),
    ]
