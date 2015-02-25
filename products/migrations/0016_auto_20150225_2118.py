# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20150222_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='production_id',
            field=models.CharField(default=0, max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='production',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
            preserve_default=True,
        ),
    ]
