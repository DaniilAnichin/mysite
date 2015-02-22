# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150213_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='production',
            name='price_old',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
