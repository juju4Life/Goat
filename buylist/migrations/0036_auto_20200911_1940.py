# Generated by Django 3.0.5 on 2020-09-11 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buylist', '0035_auto_20200911_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buylistsubmission',
            name='payment_type',
            field=models.CharField(default='', max_length=255),
        ),
    ]
