# Generated by Django 5.0.6 on 2024-07-02 21:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_auto_camion_camioneta_moto_remove_cliente_domicilio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='uploadDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='camion',
            name='uploadDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='camioneta',
            name='uploadDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='moto',
            name='uploadDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]