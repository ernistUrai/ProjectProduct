# Generated by Django 5.1.4 on 2024-12-09 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_cart_created_data_alter_cart_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_data',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
