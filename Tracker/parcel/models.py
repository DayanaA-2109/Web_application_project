from django.db import models

class Parcel(models.Model):
    parcel_id = models.AutoField(primary_key=True)

    tracking_id = models.CharField(max_length=20)
    parcel_type = models.CharField(max_length=20)

    sender_name = models.CharField(max_length=100)
    sender_phone = models.CharField(max_length=15)

    receiver_name = models.CharField(max_length=100)
    receiver_phone = models.CharField(max_length=15)

    product_name = models.CharField(max_length=100, blank=True, null=True)

    weight = models.DecimalField(max_digits=5, decimal_places=2)

    booking_date = models.DateTimeField()

    current_status = models.CharField(max_length=50)

    class Meta:
        db_table = 'parcel'
        managed = False