# Generated by Django 2.1.4 on 2019-04-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0107_auto_20190330_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtgforeign',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='mtgforeign',
            name='product_id',
        ),
        migrations.AlterField(
            model_name='updatedinventory',
            name='change_date',
            field=models.CharField(default='Mon/01/2019', max_length=255, verbose_name='Price Changed on'),
        ),
    ]