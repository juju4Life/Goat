# Generated by Django 2.2.2 on 2019-11-26 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0138_auto_20191123_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpricedata',
            name='low_store_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cardpricedata',
            name='printing',
            field=models.CharField(default='', max_length=255),
        ),
    ]