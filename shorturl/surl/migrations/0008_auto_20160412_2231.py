# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surl', '0007_auto_20160412_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='word_ind',
            field=models.IntegerField(null=True),
        ),
    ]
