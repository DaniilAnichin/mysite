# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150213_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='id',
            field=models.IntegerField(serialize=False, default=0, primary_key=True, max_length=10),
            preserve_default=True,
        ),
    ]
