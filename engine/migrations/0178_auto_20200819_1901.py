# Generated by Django 3.0.5 on 2020-08-19 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0177_mtgdatabase_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mtgdatabase',
            name='sku',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]