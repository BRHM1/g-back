# Generated by Django 4.2.5 on 2025-01-22 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_order_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='customer',
        ),
    ]
