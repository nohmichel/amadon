# Generated by Django 3.1.7 on 2021-03-16 03:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('poorly_coded_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Product',
            field=models.ForeignKey(default= 1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='poorly_coded_store.product'),
            preserve_default=False,
        ),
    ]