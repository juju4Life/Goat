# Generated by Django 3.0.5 on 2020-09-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0184_auto_20200928_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='SickDeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('expansion', models.CharField(default='', max_length=255)),
                ('printing', models.CharField(default='', max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, null=True)),
                ('image', models.CharField(default='no_image.png', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
