# Generated by Django 2.1.4 on 2019-04-12 00:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0160_auto_20190406_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 11, 20, 44, 58, 822892), verbose_name='Order Placed'),
        ),
    ]
