# Generated by Django 2.0 on 2018-09-19 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0038_auto_20180919_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 19, 19, 45, 22, 999712), verbose_name='Order Placed'),
        ),
    ]
