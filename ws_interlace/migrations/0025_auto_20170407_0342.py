# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws_interlace', '0024_auto_20170407_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image_file',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]