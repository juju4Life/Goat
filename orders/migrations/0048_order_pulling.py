# Generated by Django 3.0.5 on 2020-06-20 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0047_orderslayout_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pulling',
            field=models.BooleanField(default=False),
        ),
    ]