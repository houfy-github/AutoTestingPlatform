# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-02-20 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_project_setting',
            name='host',
            field=models.CharField(max_length=100),
        ),
    ]
