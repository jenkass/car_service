# Generated by Django 3.1.4 on 2020-12-18 18:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(9999.99), django.core.validators.MinValueValidator(1)], verbose_name='Цена'),
        ),
    ]
