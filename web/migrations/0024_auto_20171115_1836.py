# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_auto_20171115_1822'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='continiuingBTstudents',
            new_name='continuingBTstudents',
        ),
        migrations.RenameField(
            model_name='continuingbtstudents',
            old_name='continiuingBTstudents',
            new_name='continuingBTstudents',
        ),
    ]