# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 00:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171201_0344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='group',
        ),
        migrations.AddField(
            model_name='profile',
            name='groups',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]