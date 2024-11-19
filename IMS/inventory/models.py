from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ("AC Compressors", "AC Compressors"),
    ("Alternators", "Alternators"),
    ("Brake Boosters/Master Cylinders", "Brake Boosters/Master Cylinders"),
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
    ("Water Pumps", "Water Pumps")
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address = models.CharField(max_length=40, null=True)
    mobile = models.CharField(max_length=12, null=True)
    picture = models.ImageField(default="avatar.jpeg", upload_to="Pictures")

    def __str__(self) -> str:
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    product_name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    address = models.TextField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self) -> str:
        return f"{self.product} ordered quantity {self.order_quantity}"


class Notification(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.item.part_name}"