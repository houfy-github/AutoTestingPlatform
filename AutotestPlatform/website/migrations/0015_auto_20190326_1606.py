# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-03-26 08:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_ui_test_plan_browsers_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ui_test_plan',
            old_name='browsers_id',
            new_name='browser_id',
        ),
    ]
