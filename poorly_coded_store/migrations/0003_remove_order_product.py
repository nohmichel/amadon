# Generated by Django 3.1.7 on 2021-03-16 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poorly_coded_store', '0002_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Product',
        ),
    ]
