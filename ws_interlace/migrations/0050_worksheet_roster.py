# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws_interlace', '0049_auto_20170504_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksheet',
            name='roster',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
