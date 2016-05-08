# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sign',
            options={'verbose_name': 'Soul Sign', 'verbose_name_plural': 'Soul Signs'},
        ),
        migrations.RenameField(
            model_name='sign',
            old_name='timestamp',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='sign',
            name='expire_datetime',
        ),
        migrations.AddField(
            model_name='sign',
            name='expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]