# Generated by Django 4.2.5 on 2025-01-22 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_orderitem_order_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='shop.address'),
            preserve_default=False,
        ),
    ]
