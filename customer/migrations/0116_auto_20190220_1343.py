# Generated by Django 2.1.4 on 2019-02-20 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0115_auto_20190219_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 13, 43, 42, 734862), verbose_name='Order Placed'),
        ),
    ]
