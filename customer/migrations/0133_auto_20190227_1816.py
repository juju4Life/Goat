# Generated by Django 2.1.4 on 2019-02-27 23:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0132_auto_20190227_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 27, 18, 16, 51, 784078), verbose_name='Order Placed'),
        ),
    ]