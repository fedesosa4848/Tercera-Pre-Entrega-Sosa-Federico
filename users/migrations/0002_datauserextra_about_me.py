# Generated by Django 5.0.6 on 2024-07-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datauserextra',
            name='about_me',
            field=models.TextField(blank=True, default=''),
        ),
    ]