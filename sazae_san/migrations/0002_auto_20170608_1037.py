# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-08 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sazae_san', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='hand',
            field=models.CharField(choices=[('ROCK', 'ROCK'), ('SESSERS', 'SESSERS'), ('PAPER', 'PAPER')], max_length=7),
        ),
    ]
