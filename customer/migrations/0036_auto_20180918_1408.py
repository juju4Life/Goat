# Generated by Django 2.0 on 2018-09-18 18:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0035_auto_20180917_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 18, 14, 7, 57, 253758), verbose_name='Order Placed'),
        ),
    ]
