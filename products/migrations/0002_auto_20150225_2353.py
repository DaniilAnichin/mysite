# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size_text', models.CharField(default=0, max_length=100)),
                ('production', models.ForeignKey(to='products.Production')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='production',
            name='sizes',
        ),
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
