# Generated by Django 4.2.5 on 2025-01-29 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_address_first_street_alter_address_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='title_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
