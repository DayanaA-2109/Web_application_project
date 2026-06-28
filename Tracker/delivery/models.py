from django.db import models

class Delivery(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Packed', 'Packed'),
        ('Shipped', 'Shipped'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    tracking_number = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    delivery_date = models.DateField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tracking_number