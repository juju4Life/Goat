# Generated by Django 3.0.5 on 2020-07-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0055_auto_20200706_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedorder',
            name='country',
            field=models.CharField(blank=True, default='US', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, default='US', max_length=255),
        ),
        migrations.AddField(
            model_name='pendingpaymentorder',
            name='country',
            field=models.CharField(blank=True, default='US', max_length=255),
        ),
        migrations.AddField(
            model_name='pullingorder',
            name='country',
            field=models.CharField(blank=True, default='US', max_length=255),
        ),
        migrations.AddField(
            model_name='readytoshiporder',
            name='country',
            field=models.CharField(blank=True, default='US', max_length=255),
        ),
    ]
