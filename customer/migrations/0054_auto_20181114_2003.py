# Generated by Django 2.0 on 2018-11-15 01:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0053_auto_20181114_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 20, 3, 6, 238806), verbose_name='Order Placed'),
        ),
    ]
