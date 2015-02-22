# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('location_text', models.CharField(max_length=200)),
                ('arrivals_date', models.DateTimeField(verbose_name='date arrived')),
                ('departure_date', models.DateTimeField(verbose_name='date departured')),
                ('friend', models.ForeignKey(to='friends_mapping.Friend')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
