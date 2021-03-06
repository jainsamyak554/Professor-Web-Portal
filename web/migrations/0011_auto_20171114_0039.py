# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20171112_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='education',
            name='info',
        ),
        migrations.RemoveField(
            model_name='work',
            name='info',
        ),
        migrations.RemoveField(
            model_name='info',
            name='Department',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
        migrations.AddField(
            model_name='info',
            name='Dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Department'),
        ),
    ]
