# Generated by Django 2.2.2 on 2020-01-04 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buylist', '0028_auto_20200103_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storecredit',
            name='customer_name',
        ),
        migrations.AlterField(
            model_name='storecredit',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]