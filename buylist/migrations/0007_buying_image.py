# Generated by Django 2.0 on 2018-08-10 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buylist', '0006_remove_buying_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='buying',
            name='image',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
