# Generated by Django 5.1.3 on 2024-11-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0004_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
