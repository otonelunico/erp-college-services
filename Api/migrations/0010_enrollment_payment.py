# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_remove_student_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='payment',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
    ]
