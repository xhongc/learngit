# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-25 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20180525_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join_time',
            name='event_status',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='活动状态'),
        ),
    ]