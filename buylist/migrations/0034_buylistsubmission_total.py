# Generated by Django 3.0.5 on 2020-09-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buylist', '0033_buylistsubmission_paypal_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='buylistsubmission',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
