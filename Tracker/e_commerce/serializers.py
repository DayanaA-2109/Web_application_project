from .models import User, Shipment, Tracking, ApiKey, Invoice


# ==========================================
# USER SERIALIZER
# ==========================================

class UserSerializer:

    @staticmethod
    def serialize(user):

        return {

            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role,
            "company_name": user.company_name,
            "city": user.city,
            "pincode": user.pincode,
            "is_active": user.is_active,
            "created_at": user.created_at

        }

    @staticmethod
    def serialize_many(users):

        return [UserSerializer.serialize(user) for user in users]


# ==========================================
# SHIPMENT SERIALIZER
# ==========================================

class ShipmentSerializer:

    @staticmethod
    def serialize(shipment):

        return {

            "id": shipment.id,

            "awb_number": shipment.awb_number,

            "merchant_id": shipment.merchant_id,

            "merchant_name": shipment.merchant.name if shipment.merchant else None,

            "order_id": shipment.order_id,

            "receiver_name": shipment.receiver_name,

            "receiver_phone": shipment.receiver_phone,

            "receiver_address": shipment.receiver_address,

            "receiver_city": shipment.receiver_city,

            "receiver_pincode": shipment.receiver_pincode,

            "weight": float(shipment.weight),

            "cod_amount": float(shipment.cod_amount),

            "status": shipment.status,

            "assigned_agent_id": shipment.assigned_agent_id,

            "expected_delivery": shipment.expected_delivery,

            "delivered_at": shipment.delivered_at,

            "created_at": shipment.created_at

        }

    @staticmethod
    def serialize_many(shipments):

        return [
            ShipmentSerializer.serialize(shipment)
            for shipment in shipments
        ]


# ==========================================
# TRACKING SERIALIZER
# ==========================================

class TrackingSerializer:

    @staticmethod
    def serialize(track):

        return {

            "id": track.id,

            "shipment_id": track.shipment_id,

            "awb_number": track.shipment.awb_number,

            "status": track.status,

            "location": track.location,

            "latitude": float(track.latitude) if track.latitude else None,

            "longitude": float(track.longitude) if track.longitude else None,

            "remarks": track.remarks,

            "created_at": track.created_at

        }

    @staticmethod
    def serialize_many(tracks):

        return [
            TrackingSerializer.serialize(track)
            for track in tracks
        ]


# ==========================================
# API KEY SERIALIZER
# ==========================================

class ApiKeySerializer:

    @staticmethod
    def serialize(key):

        return {

            "id": key.id,

            "merchant_id": key.merchant_id,

            "merchant_name": key.merchant.name if key.merchant else None,

            "key_name": key.key_name,

            "api_key": key.api_key,

            "permissions": key.permissions,

            "is_active": key.is_active,

            "last_used": key.last_used,

            "created_at": key.created_at

        }

    @staticmethod
    def serialize_many(keys):

        return [
            ApiKeySerializer.serialize(key)
            for key in keys
        ]


# ==========================================
# INVOICE SERIALIZER
# ==========================================

class InvoiceSerializer:

    @staticmethod
    def serialize(invoice):

        return {

            "id": invoice.id,

            "merchant_id": invoice.merchant_id,

            "merchant_name": invoice.merchant.name if invoice.merchant else None,

            "invoice_number": invoice.invoice_number,

            "total_amount": float(invoice.total_amount),

            "status": invoice.status,

            "due_date": invoice.due_date,

            "paid_at": invoice.paid_at,

            "created_at": invoice.created_at

        }

    @staticmethod
    def serialize_many(invoices):

        return [
            InvoiceSerializer.serialize(invoice)
            for invoice in invoices
        ]