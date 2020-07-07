# Generated by Django 3.0.5 on 2020-07-06 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0278_auto_20200706_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(blank=True, default='US', max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='second_country',
            field=models.CharField(blank=True, default='US', max_length=255),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='country',
            field=models.CharField(blank=True, default='US', max_length=255),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='second_country',
            field=models.CharField(blank=True, default='US', max_length=255),
        ),
    ]
