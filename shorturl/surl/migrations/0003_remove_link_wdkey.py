# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surl', '0002_auto_20160412_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='wdkey',
        ),
    ]