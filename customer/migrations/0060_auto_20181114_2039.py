# Generated by Django 2.0 on 2018-11-15 01:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0059_auto_20181114_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 20, 39, 56, 616440), verbose_name='Order Placed'),
        ),
    ]
