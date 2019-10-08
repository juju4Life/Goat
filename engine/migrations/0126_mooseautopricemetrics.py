# Generated by Django 2.2.2 on 2019-09-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0125_mooseinventory_updated_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='MooseAutopriceMetrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('expansion', models.CharField(default='', max_length=255)),
                ('condition', models.CharField(default='', max_length=255)),
                ('printing', models.CharField(default='', max_length=255)),
                ('updated_price', models.CharField(default='', max_length=255)),
                ('old_price', models.CharField(default='', max_length=255)),
                ('price_1', models.CharField(default='', max_length=255)),
                ('price_1_gold', models.BooleanField(default=False)),
                ('price_2', models.CharField(default='', max_length=255)),
                ('price_2_gold', models.BooleanField(default=False)),
                ('price_3', models.CharField(default='', max_length=255)),
                ('price_3_gold', models.BooleanField(default=False)),
                ('price_4', models.CharField(default='', max_length=255)),
                ('price_4_gold', models.BooleanField(default=False)),
                ('price_5', models.CharField(default='', max_length=255)),
                ('price_5_gold', models.BooleanField(default=False)),
            ],
        ),
    ]