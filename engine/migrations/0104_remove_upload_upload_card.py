# Generated by Django 2.1.4 on 2019-03-05 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0103_auto_20190305_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='upload_card',
        ),
    ]
