# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150213_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='production',
            name='price_old',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=True,
        ),
    ]
