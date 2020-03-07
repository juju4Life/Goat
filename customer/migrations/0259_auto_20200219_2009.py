# Generated by Django 2.2.2 on 2020-02-20 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0258_auto_20200219_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='medal',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='tournament_entry',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='tournament_results_credit',
        ),
        migrations.RemoveField(
            model_name='historicalcustomer',
            name='medal',
        ),
        migrations.RemoveField(
            model_name='historicalcustomer',
            name='tournament_entry',
        ),
        migrations.RemoveField(
            model_name='historicalcustomer',
            name='tournament_results_credit',
        ),
        migrations.AddField(
            model_name='customer',
            name='login_attempt_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='login_attempt_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 20, 9, 39, 952145), verbose_name='Order Placed'),
        ),
    ]