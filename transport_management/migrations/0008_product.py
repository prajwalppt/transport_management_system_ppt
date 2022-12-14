# Generated by Django 3.1.13 on 2022-08-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport_management', '0007_vehiclemaintanance_under_maintanance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('weight_in_kg', models.PositiveIntegerField()),
                ('rate', models.PositiveIntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
