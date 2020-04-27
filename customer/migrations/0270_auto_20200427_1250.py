# Generated by Django 3.0.5 on 2020-04-27 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0269_auto_20200424_0619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpreordersready',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='historicalpreordersready',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalpreordersready',
            name='product',
        ),
        migrations.DeleteModel(
            name='ItemizedPreorder',
        ),
        migrations.DeleteModel(
            name='OrderRequest',
        ),
        migrations.RemoveField(
            model_name='preordersready',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='preordersready',
            name='product',
        ),
        migrations.DeleteModel(
            name='ReleasedProducts',
        ),
        migrations.DeleteModel(
            name='HistoricalPreordersReady',
        ),
        migrations.DeleteModel(
            name='Preorder',
        ),
        migrations.DeleteModel(
            name='PreordersReady',
        ),
    ]
