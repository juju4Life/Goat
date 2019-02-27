# Generated by Django 2.1.4 on 2019-02-27 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_neworders_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neworders',
            name='check_order_date',
        ),
        migrations.AddField(
            model_name='neworders',
            name='order_delivery_type',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]