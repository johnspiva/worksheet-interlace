# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws_interlace', '0048_remove_answer_collaborators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(blank=True, default='-', max_length=100),
        ),
    ]