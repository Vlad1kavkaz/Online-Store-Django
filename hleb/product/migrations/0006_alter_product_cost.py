# Generated by Django 4.2.2 on 2023-07-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.IntegerField(default=0, null=True, verbose_name='Цена'),
        ),
    ]
