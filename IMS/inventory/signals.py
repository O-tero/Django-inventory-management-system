from django.db.models.signals import post_save
from django.dispatch import receiver
from inventory.models import Product, Notification

@receiver(post_save, sender=InventoryItem)
def check_low_stock(sender, instance, **kwargs):
    if instance.quantity_in_stock < 10: 
        Notification.objects.create(
            message=f"Stock for {instance.part_name} is low.",
            item=instance
        )
