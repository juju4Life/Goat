# Generated by Django 2.2.2 on 2019-08-12 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0187_auto_20190808_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 12, 15, 28, 36, 955020), verbose_name='Order Placed'),
        ),
    ]
