# Generated by Django 2.1.4 on 2019-03-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EbayAccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('token', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='EbayListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=80)),
                ('sku', models.CharField(default='', max_length=25)),
                ('listing_id', models.CharField(default='', max_length=30, unique=True)),
                ('payment_policy_id', models.CharField(default='', max_length=30)),
                ('category_id', models.CharField(default='', max_length=30)),
                ('fulfillment_policy_id', models.CharField(default='', max_length=30)),
                ('return_policy_id', models.CharField(default='', max_length=30)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('description', models.TextField(default='')),
                ('format', models.CharField(default='', max_length=20)),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
            ],
        ),
    ]