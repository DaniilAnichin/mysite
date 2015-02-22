# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20150215_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick_name', models.CharField(max_length=200)),
                ('is_logged', models.BooleanField(default=False)),
                ('balans', models.IntegerField(default=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
