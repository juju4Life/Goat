# Generated by Django 3.0.5 on 2020-09-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buylist', '0030_buylistsubmission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buylistsubmission',
            name='expansion',
        ),
        migrations.RemoveField(
            model_name='buylistsubmission',
            name='language',
        ),
        migrations.RemoveField(
            model_name='buylistsubmission',
            name='name',
        ),
        migrations.RemoveField(
            model_name='buylistsubmission',
            name='price',
        ),
        migrations.RemoveField(
            model_name='buylistsubmission',
            name='quantity',
        ),
        migrations.AddField(
            model_name='buylistsubmission',
            name='buylist_number',
            field=models.TextField(default='', max_length=255),
        ),
    ]