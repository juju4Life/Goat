# Generated by Django 2.2.2 on 2020-02-19 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0256_auto_20200219_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 14, 28, 21, 464024), verbose_name='Order Placed'),
        ),
    ]