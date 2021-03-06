# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskexecution',
            name='day_order',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='estimated_duration',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='taskexecution',
            name='duration',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4),
        ),
    ]
