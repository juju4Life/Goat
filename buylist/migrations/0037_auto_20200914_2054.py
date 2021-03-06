# Generated by Django 3.0.5 on 2020-09-15 00:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buylist', '0036_auto_20200911_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='starcitybuylist',
            old_name='price_hp',
            new_name='price_ex',
        ),
        migrations.RenameField(
            model_name='starcitybuylist',
            old_name='price_played',
            new_name='price_vg',
        ),
        migrations.AddField(
            model_name='buylistsubmission',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
