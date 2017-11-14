# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.BooleanField(verbose_name='Liked')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='prod.User')),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='prod.Product')),
            ],
        ),
    ]
