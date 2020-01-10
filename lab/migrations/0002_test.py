# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-07 09:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('lab', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lab.Lab')),
            ],
        ),
    ]
