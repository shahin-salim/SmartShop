# Generated by Django 3.2 on 2022-01-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0011_alter_products_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='quantity',
        ),
        migrations.AddField(
            model_name='variantandprice',
            name='quantity',
            field=models.IntegerField(default=10),
        ),
    ]
