# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dex_num', models.IntegerField(blank=True, null=True)),
                ('species', models.CharField(max_length=200)),
                ('type1', models.CharField(max_length=200)),
                ('type2', models.CharField(max_length=200)),
                ('is_caught', models.BooleanField(default=False)),
            ],
        ),
    ]
