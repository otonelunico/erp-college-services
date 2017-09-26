# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_remove_qualification_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rode', models.IntegerField()),
                ('tariff', models.IntegerField()),
                ('monthly', models.IntegerField()),
                ('total', models.IntegerField()),
                ('remaining', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('period', models.IntegerField()),
                ('grade', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Api.Grade')),
                ('student', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Api.Student')),
            ],
        ),
        migrations.RenameField(
            model_name='qualification',
            old_name='periodo',
            new_name='period',
        ),
    ]
