# Generated by Django 2.2.2 on 2019-09-28 20:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0201_auto_20190927_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 28, 16, 45, 22, 321197), verbose_name='Order Placed'),
        ),
    ]