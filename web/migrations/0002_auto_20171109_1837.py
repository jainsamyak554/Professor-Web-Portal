# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 13:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='office',
            new_name='room',
        ),
    ]
