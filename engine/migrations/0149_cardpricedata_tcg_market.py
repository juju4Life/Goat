# Generated by Django 2.2.2 on 2020-01-06 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0148_auto_20200103_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpricedata',
            name='tcg_market',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12),
        ),
    ]