# Generated by Django 2.0 on 2018-09-06 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0020_auto_20180825_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='credit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, verbose_name='Store Credit'),
        ),
        migrations.AlterField(
            model_name='historicalcustomer',
            name='credit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, verbose_name='Store Credit'),
        ),
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 11, 55, 8, 770591), verbose_name='Order Placed'),
        ),
        migrations.AlterField(
            model_name='orderrequest',
            name='order_link',
            field=models.URLField(blank=True, default='', max_length=5000),
        ),
    ]
