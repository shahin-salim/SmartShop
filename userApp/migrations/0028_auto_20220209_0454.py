# Generated by Django 3.2 on 2022-02-09 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0024_alter_products_processor'),
        ('userApp', '0027_order_coupen_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='guest_user',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='variant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminApp.variantandprice'),
        ),
    ]
