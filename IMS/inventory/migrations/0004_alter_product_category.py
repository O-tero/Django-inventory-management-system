# Generated by Django 5.1.3 on 2024-11-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0003_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("AC Compressors", "AC Compressors"),
                    ("Alternators", "Alternators"),
                    (
                        "Brake Boosters/Master Cylinders",
                        "Brake Boosters/Master Cylinders",
                    ),
                    ("Common Rail Injectors", "Common Rail Injectors"),
                    ("Engines", "Engines"),
                    ("Engine Oils", "Engine Oils"),
                    ("Fog Lights", "Fog Lights"),
                    ("Hybrid car Parts", "Hybrid car Parts"),
                    ("Injector Nozzles", "Injector Nozzles"),
                    ("Injector Pumps", "Injector Pumps"),
                    ("Mounts", "Mounts"),
                    ("Other Popular Parts", "Other Popular Parts"),
                    ("Power Steering Parts", "Power Steering Parts"),
                    ("Rear Axle Beams", "Rear Axle Beams"),
                    ("Stabilizer Bars", "Stabilizer Bars"),
                    ("Starter Motors", "Starter Motors"),
                    ("Steering Racks", "Steering Racks"),
                    ("Throttle Bodies", "Throttle Bodies"),
                    ("Transmission Fluids", "Transmission Fluids"),
                    ("Transmissions/Gearboxes", "Transmissions/Gearboxes"),
                    ("Turbochargers", "Turbochargers"),
                    ("Water Pumps", "Water Pumps"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
