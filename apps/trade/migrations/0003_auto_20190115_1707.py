# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-15 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20190115_1544'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ordergoods',
            table='s_order_goods',
        ),
        migrations.AlterModelTable(
            name='orderinfo',
            table='s_ordings',
        ),
        migrations.AlterModelTable(
            name='shoppingcart',
            table='s_shopping_cart',
        ),
    ]
