# Generated by Django 2.1.4 on 2019-01-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0083_auto_20190123_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindatabase',
            name='foil_select',
            field=models.CharField(choices=[('non-foil', 'Non-foil'), ('foil', 'foil')], default=('foil', 'foil'), max_length=10),
        ),
    ]
