# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_auto_20170925_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualification',
            name='detail',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]