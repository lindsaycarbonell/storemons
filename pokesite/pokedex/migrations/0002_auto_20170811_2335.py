# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='dex_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='species',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type1',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
