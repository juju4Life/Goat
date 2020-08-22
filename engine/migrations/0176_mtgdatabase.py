# Generated by Django 3.0.5 on 2020-08-19 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0175_mtg_solid_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTGDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=255)),
                ('expansion', models.CharField(db_index=True, default='', max_length=255)),
                ('sku', models.CharField(default='', max_length=255)),
                ('printing', models.CharField(default='', max_length=255)),
                ('condition', models.CharField(default='', max_length=255)),
                ('language', models.CharField(default='', max_length=255)),
                ('stock', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
            ],
        ),
    ]
