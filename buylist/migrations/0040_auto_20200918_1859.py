# Generated by Django 3.0.5 on 2020-09-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buylist', '0039_buylistsubmission_order_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='buylistsubmission',
            name='seller_review_grading',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='buylistsubmission',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]