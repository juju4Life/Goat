# Generated by Django 2.2.2 on 2019-10-07 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0203_auto_20190928_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 7, 16, 36, 16, 631141), verbose_name='Order Placed'),
        ),
    ]