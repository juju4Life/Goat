# Generated by Django 2.1.4 on 2018-12-29 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0072_auto_20181226_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 29, 11, 23, 29, 450732), verbose_name='Order Placed'),
        ),
    ]