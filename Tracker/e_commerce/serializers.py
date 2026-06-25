# e_commerce/serializers.py

from .models import User, Shipment, Tracking


class UserSerializer:
    """Convert User model to JSON"""

    @staticmethod
    def serialize(user):
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'role': user.role,
            'company_name': user.company_name,
            'city': user.city,
            'pincode': user.pincode,
            'is_active': user.is_active,
            'created_at': user.created_at
        }

    @staticmethod
    def serialize_many(users):
        return [UserSerializer.serialize(user) for user in users]


class ShipmentSerializer:
    """Convert Shipment model to JSON"""

    @staticmethod
    def serialize(shipment):
        return {
            'id': shipment.id,
            'awb_number': shipment.awb_number,
            'merchant': shipment.merchant.id,
            'merchant_name': shipment.merchant.name if shipment.merchant else None,
            'order_id': shipment.order_id,
            'receiver_name': shipment.receiver_name,
            'receiver_phone': shipment.receiver_phone,
            'receiver_address': shipment.receiver_address,
            'receiver_city': shipment.receiver_city,
            'receiver_pincode': shipment.receiver_pincode,
            'weight': str(shipment.weight),
            'cod_amount': str(shipment.cod_amount),
            'status': shipment.status,
            'status_display': dict(Shipment.STATUS_CHOICES).get(shipment.status, shipment.status),
            'assigned_agent': shipment.assigned_agent.id if shipment.assigned_agent else None,
            'agent_name': shipment.assigned_agent.name if shipment.assigned_agent else None,
            'expected_delivery': shipment.expected_delivery,
            'delivered_at': shipment.delivered_at,
            'created_at': shipment.created_at
        }

    @staticmethod
    def serialize_many(shipments):
        return [ShipmentSerializer.serialize(s) for s in shipments]


class TrackingSerializer:
    """Convert Tracking model to JSON"""

    @staticmethod
    def serialize(tracking):
        return {
            'id': tracking.id,
            'shipment': tracking.shipment.id,
            'awb_number': tracking.shipment.awb_number,
            'status': tracking.status,
            'location': tracking.location,
            'remarks': tracking.remarks,
            'created_at': tracking.created_at
        }

    @staticmethod
    def serialize_many(tracking_entries):
        return [TrackingSerializer.serialize(t) for t in tracking_entries]