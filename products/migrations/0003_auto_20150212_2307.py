# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150212_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='price',
            field=models.DecimalField(max_digits=10, default=0, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='production',
            name='price_old',
            field=models.DecimalField(max_digits=10, default=0, decimal_places=2),
            preserve_default=True,
        ),
    ]
