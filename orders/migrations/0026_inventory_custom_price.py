# Generated by Django 2.1.4 on 2019-03-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20190303_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='custom_price',
            field=models.BooleanField(default=False),
        ),
    ]
