# Generated by Django 2.0 on 2018-09-17 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0034_auto_20180917_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 17, 11, 29, 42, 257574), verbose_name='Order Placed'),
        ),
    ]
