from django.test import TestCase
from .models import Delivery


class DeliveryModelTest(TestCase):

    def setUp(self):
        self.delivery = Delivery.objects.create(
            customer_name="John Doe",
            product_name="Laptop",
            quantity=2,
            address="Chennai, Tamil Nadu",
            status="Pending"
        )

    def test_delivery_creation(self):
        self.assertEqual(self.delivery.customer_name, "John Doe")
        self.assertEqual(self.delivery.product_name, "Laptop")
        self.assertEqual(self.delivery.quantity, 2)
        self.assertEqual(self.delivery.address, "Chennai, Tamil Nadu")
        self.assertEqual(self.delivery.status, "Pending")

    def test_string_representation(self):
        self.assertEqual(str(self.delivery), "John Doe")

    def test_status_update(self):
        self.delivery.status = "Delivered"
        self.delivery.save()

        updated = Delivery.objects.get(id=self.delivery.id)
        self.assertEqual(updated.status, "Delivered")

    def test_delete_delivery(self):
        delivery_id = self.delivery.id
        self.delivery.delete()

        self.assertFalse(
            Delivery.objects.filter(id=delivery_id).exists()
        )