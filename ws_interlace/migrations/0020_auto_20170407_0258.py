# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 02:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ws_interlace', '0019_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='answer',
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]
