# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20171115_0125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publications',
            old_name='pub',
            new_name='publication',
        ),
        migrations.RemoveField(
            model_name='info',
            name='publ',
        ),
        migrations.AddField(
            model_name='publications',
            name='publication_details',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
