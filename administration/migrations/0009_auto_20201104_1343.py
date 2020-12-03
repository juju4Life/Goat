# Generated by Django 3.0.5 on 2020-11-04 18:43

from django.db import migrations, models
import validators.model_validators


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0008_auto_20201028_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safe',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=12),
        ),
        migrations.AlterField(
            model_name='safe',
            name='deposit',
            field=models.CharField(default='0', editable=False, max_length=12, validators=[validators.model_validators.contains_plus]),
        ),
        migrations.AlterField(
            model_name='safe',
            name='manager_initials',
            field=models.CharField(default='', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='safe',
            name='withdrawal',
            field=models.CharField(default='0', editable=False, max_length=12, validators=[validators.model_validators.contains_minus]),
        ),
    ]