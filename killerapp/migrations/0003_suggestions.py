# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('killerapp', '0002_auto_20160630_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Suggestions', models.CharField(max_length=1000)),
            ],
        ),
    ]
