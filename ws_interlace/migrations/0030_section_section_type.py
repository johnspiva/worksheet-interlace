# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws_interlace', '0029_remove_answer_section_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='section_type',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
