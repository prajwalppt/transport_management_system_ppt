# Generated by Django 3.1.13 on 2022-08-01 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport_management', '0009_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='location_from',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='booking',
            name='location_to',
            field=models.CharField(max_length=70),
        ),
    ]
