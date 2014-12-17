# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_number', models.IntegerField(default=0)),
                ('house_characters', models.CharField(default='', max_length=3)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostCode',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_nominative', models.CharField(max_length=48, db_index=True)),
                ('name_genitive', models.CharField(max_length=48, db_index=True)),
                ('postcode', models.ForeignKey(to='ice_addresses.PostCode')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.ForeignKey(to='ice_addresses.Street'),
            preserve_default=True,
        ),
    ]
