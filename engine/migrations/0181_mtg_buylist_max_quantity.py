# Generated by Django 3.0.5 on 2020-09-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0180_mtg_buylist_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtg',
            name='buylist_max_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
