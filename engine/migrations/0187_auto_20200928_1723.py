# Generated by Django 3.0.5 on 2020-09-28 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0186_auto_20200928_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mtg',
            name='sick_deal_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sickdeal',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Percentage Off'),
        ),
    ]
