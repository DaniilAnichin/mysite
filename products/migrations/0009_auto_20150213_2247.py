# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20150213_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='id',
            field=models.CharField(max_length=6, default=0, primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
