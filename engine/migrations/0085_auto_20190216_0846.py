# Generated by Django 2.1.4 on 2019-02-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0084_auto_20190213_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatedinventory',
            name='change_date',
            field=models.CharField(default='Sat/16/2019', max_length=255, verbose_name='Price Changed on'),
        ),
    ]
