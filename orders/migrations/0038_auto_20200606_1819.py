# Generated by Django 3.0.5 on 2020-06-06 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0037_shippingmethod'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.AlterModelOptions(
            name='shippingmethod',
            options={'ordering': ['cost', 'full_name']},
        ),
    ]
