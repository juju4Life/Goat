# Generated by Django 2.2.2 on 2019-08-19 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0191_auto_20190818_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 19, 12, 13, 29, 644588), verbose_name='Order Placed'),
        ),
    ]
