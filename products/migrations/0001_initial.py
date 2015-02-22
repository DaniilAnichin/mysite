# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='production',
            fields=[
                ('name', models.CharField(default=0, max_length=200)),
                ('sizes', models.CharField(default=0, max_length=200)),
                ('price', models.CharField(default=0, max_length=10)),
                ('price_old', models.CharField(default=0, max_length=10)),
                ('id', models.CharField(serialize=False, default=0, max_length=10, primary_key=True)),
                ('delivery', models.CharField(default=0, max_length=20)),
                ('kids', models.BooleanField(default=0)),
                ('kid_adult', models.BooleanField(default=0)),
                ('free_porto', models.BooleanField(default=0)),
                ('package', models.BooleanField(default=0)),
                ('women', models.BooleanField(default=0)),
                ('url', models.URLField(default=0)),
                ('img_url', models.URLField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
