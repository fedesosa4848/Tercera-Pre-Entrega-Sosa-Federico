# Generated by Django 5.0.6 on 2024-07-05 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_auto_publicado_por_camion_publicado_por_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='camion',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='camioneta',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='moto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1000)]),
        ),
    ]