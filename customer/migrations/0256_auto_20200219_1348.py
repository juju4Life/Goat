# Generated by Django 2.2.2 on 2020-02-19 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0255_auto_20200219_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 13, 48, 17, 220133), verbose_name='Order Placed'),
        ),
    ]
