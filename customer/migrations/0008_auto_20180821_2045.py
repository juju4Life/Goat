# Generated by Django 2.0 on 2018-08-22 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20180821_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='wishlist',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='wishlist',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
