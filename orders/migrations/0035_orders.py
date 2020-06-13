# Generated by Django 3.0.5 on 2020-06-01 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0034_auto_20200427_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=255)),
                ('shipping_method', models.CharField(default='free', max_length=255)),
                ('address_line_1', models.CharField(default='', max_length=255)),
                ('address_line_2', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=255)),
                ('state', models.CharField(default='', max_length=255)),
                ('zip_code', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(blank=True, default='', max_length=255)),
                ('total_order_price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('store_credit_used', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('tax_charged', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('shipping_charged', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('discounts_applied', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('notes', models.TextField(default='')),
                ('ordered_items', models.TextField(default='')),
                ('order_view', models.URLField(default='')),
            ],
        ),
    ]
