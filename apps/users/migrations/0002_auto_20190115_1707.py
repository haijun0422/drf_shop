# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-15 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table='s_users',
        ),
        migrations.AlterModelTable(
            name='verifycode',
            table='s_verifycode',
        ),
    ]
