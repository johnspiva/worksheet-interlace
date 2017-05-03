# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ws_interlace', '0038_auto_20170421_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='student_id',
        ),
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='ws_interlace.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ManyToManyField(related_name='students', to='ws_interlace.Classroom'),
        ),
    ]
