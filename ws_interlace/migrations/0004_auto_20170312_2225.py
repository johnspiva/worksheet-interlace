# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-12 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws_interlace', '0003_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='answer',
            name='text',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
