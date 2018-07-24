# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20171115_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recognitions',
            name='recg',
        ),
        migrations.AddField(
            model_name='recognitions',
            name='recgonition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Info'),
        ),
        migrations.AddField(
            model_name='recognitions',
            name='recgonition_details',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
