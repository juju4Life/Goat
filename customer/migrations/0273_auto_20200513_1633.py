# Generated by Django 3.0.5 on 2020-05-13 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0272_remove_customer_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='restock_notice',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='customer',
            name='wishlist',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='restock_notice',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='wishlist',
            field=models.TextField(blank=True, default=''),
        ),
    ]
