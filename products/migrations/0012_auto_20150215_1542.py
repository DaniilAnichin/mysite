# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20150213_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='id',
            field=models.CharField(default=0, primary_key=True, max_length=6, serialize=False, unique=True),
            preserve_default=True,
        ),
    ]
