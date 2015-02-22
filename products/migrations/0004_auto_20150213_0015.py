# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20150212_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='price',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='production',
            name='price_old',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
