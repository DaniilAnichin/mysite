# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20150217_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bucket',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='bucket',
            name='productions',
        ),
        migrations.DeleteModel(
            name='bucket',
        ),
        migrations.DeleteModel(
            name='customer',
        ),
    ]
