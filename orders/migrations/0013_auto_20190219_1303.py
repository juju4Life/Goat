# Generated by Django 2.1.4 on 2019-02-19 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_neworders_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='last_upload_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='neworders',
            name='check_order_date',
            field=models.DateField(blank=True),
        ),
    ]
