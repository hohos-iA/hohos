# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-28 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='institute',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
