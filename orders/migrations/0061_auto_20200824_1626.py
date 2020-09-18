# Generated by Django 3.0.5 on 2020-08-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0060_auto_20200824_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedorder',
            name='missing_cards',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='missing_cards',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='pendingpaymentorder',
            name='missing_cards',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='pullingorder',
            name='missing_cards',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='readytoshiporder',
            name='missing_cards',
            field=models.TextField(blank=True, default=''),
        ),
    ]