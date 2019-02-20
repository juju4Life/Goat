# Generated by Django 2.1.4 on 2019-02-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0087_auto_20190219_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(db_index=True, default='', max_length=255)),
                ('product_line', models.CharField(default='', max_length=255)),
                ('title', models.CharField(default='', max_length=255)),
                ('rarity', models.CharField(default='', max_length=255)),
                ('number', models.IntegerField(blank=True, default=0)),
                ('set_name', models.CharField(db_index=True, default='', max_length=255)),
                ('sku', models.CharField(default='', max_length=255)),
                ('condition', models.CharField(db_index=True, default='', max_length=255)),
                ('language', models.CharField(db_index=True, default='English', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='updatedinventory',
            name='change_date',
            field=models.CharField(default='Wed/20/2019', max_length=255, verbose_name='Price Changed on'),
        ),
    ]
