# Generated by Django 3.0.5 on 2020-05-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0273_auto_20200513_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRestockNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=255)),
                ('product_id', models.CharField(default='', max_length=255)),
                ('foil', models.BooleanField(default=False)),
                ('normal', models.BooleanField(default=False)),
                ('clean', models.BooleanField(default=False)),
                ('played', models.BooleanField(default=False)),
                ('heavily_played', models.BooleanField(default=False)),
            ],
        ),
    ]
