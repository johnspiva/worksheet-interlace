# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 22:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ws_interlace', '0010_remove_worksheet_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='slug',
        ),
    ]
