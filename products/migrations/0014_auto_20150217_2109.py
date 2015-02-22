# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='bucket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_empty', models.BooleanField(default=True)),
                ('cost', models.IntegerField(default=0)),
                ('customer', models.OneToOneField(to='products.customer')),
                ('productions', models.ManyToManyField(to='products.production')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='nick_name',
            new_name='nickname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='balans',
        ),
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
