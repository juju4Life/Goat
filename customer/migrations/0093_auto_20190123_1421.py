# Generated by Django 2.1.4 on 2019-01-23 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0092_auto_20190123_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 14, 21, 28, 285276), verbose_name='Order Placed'),
        ),
    ]