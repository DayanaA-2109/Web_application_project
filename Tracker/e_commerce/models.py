from django.db import models


# ==========================
# USERS
# ==========================

class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    role = models.CharField(max_length=20)

    company_name = models.CharField(max_length=150, blank=True, null=True)

    city = models.CharField(max_length=50, blank=True, null=True)

    pincode = models.CharField(max_length=10, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "users_ecommerce"

    def __str__(self):
        return self.name


# ==========================
# SHIPMENTS
# ==========================

class Shipment(models.Model):

    STATUS_CHOICES = [

        ('pending', 'Pending'),
        ('picked_up', 'Picked Up'),
        ('in_transit', 'In Transit'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
    ]

    id = models.AutoField(primary_key=True)

    awb_number = models.CharField(max_length=20)

    merchant = models.ForeignKey(
        User,
        db_column="merchant_id",
        on_delete=models.CASCADE
    )

    order_id = models.CharField(max_length=100, blank=True, null=True)

    receiver_name = models.CharField(max_length=100)

    receiver_phone = models.CharField(max_length=20)

    receiver_address = models.TextField()

    receiver_city = models.CharField(max_length=50)

    receiver_pincode = models.CharField(max_length=10)

    weight = models.DecimalField(max_digits=8, decimal_places=2)

    cod_amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES
    )

    assigned_agent_id = models.IntegerField(blank=True, null=True)

    expected_delivery = models.DateField(blank=True, null=True)

    delivered_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "shipments"

    def __str__(self):
        return self.awb_number


# ==========================
# TRACKING
# ==========================

class Tracking(models.Model):

    id = models.AutoField(primary_key=True)

    shipment = models.ForeignKey(
        Shipment,
        db_column="shipment_id",
        on_delete=models.CASCADE
    )

    status = models.CharField(max_length=50)

    location = models.CharField(max_length=100)

    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "tracking"

    def __str__(self):
        return self.status


# ==========================
# API KEYS
# ==========================

class ApiKey(models.Model):

    id = models.AutoField(primary_key=True)

    merchant = models.ForeignKey(
        User,
        db_column="merchant_id",
        on_delete=models.CASCADE
    )

    key_name = models.CharField(max_length=100)

    api_key = models.CharField(max_length=64)

    permissions = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)

    last_used = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "api_keys"


# ==========================
# INVOICES
# ==========================

class Invoice(models.Model):

    id = models.AutoField(primary_key=True)

    merchant = models.ForeignKey(
        User,
        db_column="merchant_id",
        on_delete=models.CASCADE
    )

    invoice_number = models.CharField(max_length=50)

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(max_length=20)

    due_date = models.DateField()

    paid_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "invoices"