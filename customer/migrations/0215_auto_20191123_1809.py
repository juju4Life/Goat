# Generated by Django 2.2.2 on 2019-11-23 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0214_auto_20191118_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 23, 18, 9, 9, 302531), verbose_name='Order Placed'),
        ),
    ]
