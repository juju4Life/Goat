# Generated by Django 2.0 on 2018-08-10 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buylist', '0005_buying_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buying',
            name='image',
        ),
    ]
