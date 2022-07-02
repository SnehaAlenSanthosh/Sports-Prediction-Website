# Generated by Django 4.0.3 on 2022-03-13 18:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(13), django.core.validators.MaxValueValidator(19)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='sex',
            field=models.PositiveIntegerField(choices=[(0, 'Female'), (1, 'Male')], null=True),
        ),
    ]