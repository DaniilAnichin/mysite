# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150213_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True, max_length=6, default=0),
            preserve_default=True,
        ),
    ]
