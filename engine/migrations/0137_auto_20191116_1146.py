# Generated by Django 2.2.2 on 2019-11-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0136_mtg_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mooseautopricemetrics',
            name='price_1_gold',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='mooseautopricemetrics',
            name='price_2',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mooseautopricemetrics',
            name='price_2_gold',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='mooseautopricemetrics',
            name='price_3',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mooseautopricemetrics',
            name='price_4',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mooseautopricemetrics',
            name='price_4_gold',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='mooseautopricemetrics',
            name='price_5',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mooseautopricemetrics',
            name='price_5_gold',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]