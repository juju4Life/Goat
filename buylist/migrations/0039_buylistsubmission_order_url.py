# Generated by Django 3.0.5 on 2020-09-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buylist', '0038_buylistsubmission_change_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='buylistsubmission',
            name='order_url',
            field=models.URLField(blank=True),
        ),
    ]
