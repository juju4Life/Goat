# Generated by Django 2.2.2 on 2020-02-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeremail',
            name='uuid',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='customeremail',
            name='replied_at',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='customeremail',
            name='reply',
            field=models.TextField(blank=True),
        ),
    ]
