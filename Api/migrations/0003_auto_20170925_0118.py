# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_auto_20170925_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorney',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='attorney',
            name='cellphone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='attorney',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='cellphone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='cellphone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
