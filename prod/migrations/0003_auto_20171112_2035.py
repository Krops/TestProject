# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0002_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default='dron', on_delete=django.db.models.deletion.CASCADE, to='prod.User'),
        ),
    ]