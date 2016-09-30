# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_userprofile_photo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='instagram_id',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram_username',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='facebook_id',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='facebook_username',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo_url',
            field=models.TextField(default=''),
        ),
    ]