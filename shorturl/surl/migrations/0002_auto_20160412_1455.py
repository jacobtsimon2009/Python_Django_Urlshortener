# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='relate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='wdkey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='surl.relate'),
        ),
    ]
