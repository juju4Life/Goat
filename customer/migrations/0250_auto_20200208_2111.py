# Generated by Django 2.2.2 on 2020-02-09 02:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0249_auto_20200208_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 8, 21, 11, 5, 698002), verbose_name='Order Placed'),
        ),
    ]
