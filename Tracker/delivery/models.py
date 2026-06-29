from django.db import models

class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)

    user_id = models.IntegerField(null=True, blank=True)
    agent_id = models.IntegerField(null=True, blank=True)

    product_name = models.CharField(max_length=100)
    delivery_address = models.TextField()

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
    ]

    delivery_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending",
    )

    delivery_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "deliveries"
        managed = False

    def __str__(self):
        return self.product_name