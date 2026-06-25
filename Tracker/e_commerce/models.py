# e_commerce/models.py

from django.db import models


class User(models.Model):
    """Users table (users_ecommerce)"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=20)  # customer, merchant, admin, agent
    company_name = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users_ecommerce'  # ✅ Your table name
        managed = False  # ✅ Don't let Django modify it

    def __str__(self):
        return self.name


class Shipment(models.Model):
    """Shipments table"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('picked_up', 'Picked Up'),
        ('in_transit', 'In Transit'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
    ]

    id = models.AutoField(primary_key=True)
    awb_number = models.CharField(max_length=20, unique=True)
    merchant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='merchant_id'
    )
    order_id = models.CharField(max_length=100, null=True, blank=True)
    receiver_name = models.CharField(max_length=100)
    receiver_phone = models.CharField(max_length=20)
    receiver_address = models.TextField()
    receiver_city = models.CharField(max_length=50)
    receiver_pincode = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    cod_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_agent_id = models.IntegerField(null=True, blank=True)
    expected_delivery = models.DateField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shipments'
        managed = False

    def __str__(self):
        return f"{self.awb_number} - {self.receiver_name}"


class Tracking(models.Model):
    """Tracking table"""
    id = models.AutoField(primary_key=True)
    shipment = models.ForeignKey(
        Shipment,
        on_delete=models.CASCADE,
        db_column='shipment_id'
    )
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tracking'
        managed = False
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.shipment.awb_number} - {self.status}"