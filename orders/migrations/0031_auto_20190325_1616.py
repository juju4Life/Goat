# Generated by Django 2.1.4 on 2019-03-25 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_auto_20190320_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='image_url',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]