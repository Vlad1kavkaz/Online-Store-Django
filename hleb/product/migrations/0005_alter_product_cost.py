# Generated by Django 4.2.2 on 2023-07-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.IntegerField(default=0, null=True, unique=True, verbose_name='Цена'),
        ),
    ]
