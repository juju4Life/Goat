# Generated by Django 2.1.4 on 2019-03-03 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0138_auto_20190303_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 3, 17, 12, 15, 154217), verbose_name='Order Placed'),
        ),
    ]
