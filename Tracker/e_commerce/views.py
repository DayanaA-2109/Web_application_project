from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from django.db.models import Q
from django.utils import timezone

from .models import (
    User,
    Shipment,
    Tracking,
    ApiKey,
    Invoice
)

from .serializers import (
    UserSerializer,
    ShipmentSerializer,
    TrackingSerializer,
    ApiKeySerializer,
    InvoiceSerializer
)

import json
import secrets
from datetime import datetime

@require_http_methods(["GET"])
def api_test(request):

    return JsonResponse({

        "status": "success",

        "message": "E-Commerce Backend Running Successfully",

        "version": "1.0"

    })

@require_http_methods(["GET"])
def get_users(request):

    users = User.objects.filter(is_active=True)

    return JsonResponse(

        UserSerializer.serialize_many(users),

        safe=False

    )

@require_http_methods(["GET"])
def get_merchants(request):

    merchants = User.objects.filter(

        role="merchant",

        is_active=True

    )

    return JsonResponse(

        UserSerializer.serialize_many(merchants),

        safe=False

    )

@require_http_methods(["GET"])
def get_user(request, user_id):

    user = get_object_or_404(User, id=user_id)

    return JsonResponse(

        UserSerializer.serialize(user)

    )

@require_http_methods(["GET"])
def merchant_profile(request, merchant_id):

    merchant = get_object_or_404(

        User,

        id=merchant_id,

        role="merchant"

    )

    return JsonResponse(

        UserSerializer.serialize(merchant)

    )

@csrf_exempt
@require_http_methods(["PUT"])
def update_profile(request, merchant_id):

    merchant = get_object_or_404(

        User,

        id=merchant_id,

        role="merchant"

    )

    try:

        data = json.loads(request.body)

    except:

        return JsonResponse(

            {

                "error": "Invalid JSON"

            },

            status=400

        )

    merchant.name = data.get(

        "name",

        merchant.name

    )

    merchant.phone = data.get(

        "phone",

        merchant.phone

    )

    merchant.company_name = data.get(

        "company_name",

        merchant.company_name

    )

    merchant.city = data.get(

        "city",

        merchant.city

    )

    merchant.pincode = data.get(

        "pincode",

        merchant.pincode

    )

    merchant.save()

    return JsonResponse({

        "success": True,

        "message": "Profile Updated",

        "merchant": UserSerializer.serialize(merchant)

    })


@require_http_methods(["GET"])
def get_shipments(request):

    merchant = request.GET.get("merchant_id")

    search = request.GET.get("search")

    status = request.GET.get("status")

    shipments = Shipment.objects.all()

    if merchant:

        shipments = shipments.filter(

            merchant_id=merchant

        )

    if status:

        shipments = shipments.filter(

            status=status

        )

    if search:

        shipments = shipments.filter(

            Q(awb_number__icontains=search)

            |

            Q(receiver_name__icontains=search)

            |

            Q(receiver_phone__icontains=search)

        )

    shipments = shipments.order_by(

        "-created_at"

    )

    return JsonResponse(

        ShipmentSerializer.serialize_many(

            shipments

        ),

        safe=False

    )

@require_http_methods(["GET"])
def get_shipment(request, awb):

    shipment = get_object_or_404(
        Shipment,
        awb_number=awb
    )

    return JsonResponse({
        "id": shipment.id,
        "awb": shipment.awb_number,
        "receiver": shipment.receiver_name,
        "city": shipment.receiver_city,
        "status": shipment.status
    })

# ============================================
# FIXED: CREATE SHIPMENT
# ============================================

@csrf_exempt
@require_http_methods(["POST"])
def create_shipment(request):

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse(
            {"error": "Invalid JSON", "message": "Please provide valid JSON data"},
            status=400
        )

    required = [
        "merchant_id",
        "receiver_name",
        "receiver_phone",
        "receiver_address",
        "receiver_city",
        "receiver_pincode",
        "weight"
    ]

    for field in required:
        if not data.get(field):
            return JsonResponse(
                {"error": f"{field} is required", "success": False},
                status=400
            )

    merchant = get_object_or_404(
        User,
        id=data["merchant_id"]
    )

    awb = "AWB" + secrets.token_hex(5).upper()

    shipment = Shipment.objects.create(

        awb_number=awb,

        merchant=merchant,

        order_id=data.get("order_id"),

        receiver_name=data["receiver_name"],

        receiver_phone=data["receiver_phone"],

        receiver_address=data["receiver_address"],

        receiver_city=data["receiver_city"],

        receiver_pincode=data["receiver_pincode"],

        weight=data["weight"],

        cod_amount=data.get("cod_amount",0),

        status="pending",

        expected_delivery=data.get("expected_delivery"),

        created_at=timezone.now()

    )

    Tracking.objects.create(

        shipment=shipment,

        status="Shipment Created",

        location=shipment.receiver_city,

        remarks="Shipment booked",

        created_at=timezone.now()

    )

    return JsonResponse({

        "success": True,

        "message": "Shipment Created Successfully",

        "shipment": ShipmentSerializer.serialize(shipment)

    })

# ============================================
# FIXED: GENERATE API KEY
# ============================================

@csrf_exempt
@require_http_methods(["POST"])
def generate_api_key(request):

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({
            "error": "Invalid JSON",
            "success": False,
            "message": "Please provide valid JSON data"
        }, status=400)

    # Check if merchant_id is provided
    if not data.get("merchant_id"):
        return JsonResponse({
            "error": "merchant_id is required",
            "success": False,
            "message": "Merchant ID is required"
        }, status=400)

    merchant = get_object_or_404(
        User,
        id=data["merchant_id"],
        role="merchant"
    )

    key = secrets.token_hex(32)

    api = ApiKey.objects.create(

        merchant=merchant,

        key_name=data.get("key_name", "Default Key"),

        api_key=key,

        permissions="read_write",

        is_active=True,

        created_at=timezone.now()

    )

    return JsonResponse({

        "success": True,

        "message": "API Key Generated Successfully",

        "api_key": ApiKeySerializer.serialize(api)

    })


@csrf_exempt
@require_http_methods(["PUT"])
def update_shipment(request, awb):

    shipment = get_object_or_404(
        Shipment,
        awb_number=awb
    )

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse(
            {"error":"Invalid JSON"},
            status=400
        )

    shipment.receiver_name = data.get(
        "receiver_name",
        shipment.receiver_name
    )

    shipment.receiver_phone = data.get(
        "receiver_phone",
        shipment.receiver_phone
    )

    shipment.receiver_address = data.get(
        "receiver_address",
        shipment.receiver_address
    )

    shipment.receiver_city = data.get(
        "receiver_city",
        shipment.receiver_city
    )

    shipment.receiver_pincode = data.get(
        "receiver_pincode",
        shipment.receiver_pincode
    )

    shipment.weight = data.get(
        "weight",
        shipment.weight
    )

    shipment.cod_amount = data.get(
        "cod_amount",
        shipment.cod_amount
    )

    if "status" in data:
        shipment.status = data["status"]

    if shipment.status == "delivered":
        shipment.delivered_at = timezone.now()

    shipment.save()

    Tracking.objects.create(

        shipment=shipment,

        status=shipment.status,

        location=shipment.receiver_city,

        remarks="Shipment Updated",

        created_at=timezone.now()

    )

    return JsonResponse({

        "success":True,

        "shipment":ShipmentSerializer.serialize(shipment)

    })

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_shipment(request, awb):

    shipment = get_object_or_404(
        Shipment,
        awb_number=awb
    )

    shipment.delete()

    return JsonResponse({

        "success":True,

        "message":"Shipment Deleted"

    })


@require_http_methods(["GET"])
def track_shipment(request, awb):

    shipment = get_object_or_404(

        Shipment,

        awb_number=awb

    )

    tracking = Tracking.objects.filter(

        shipment=shipment

    ).order_by("-created_at")

    return JsonResponse({

        "shipment":ShipmentSerializer.serialize(shipment),

        "tracking":TrackingSerializer.serialize_many(tracking)

    })

@require_http_methods(["GET"])
def get_stats(request):

    merchant = request.GET.get("merchant_id")

    shipments = Shipment.objects.filter(
        merchant_id=merchant
    )

    return JsonResponse({

        "total":shipments.count(),

        "pending":shipments.filter(
            status="pending"
        ).count(),

        "picked_up":shipments.filter(
            status="picked_up"
        ).count(),

        "in_transit":shipments.filter(
            status="in_transit"
        ).count(),

        "delivered":shipments.filter(
            status="delivered"
        ).count(),

        "failed":shipments.filter(
            status="failed"
        ).count()

    })

@require_http_methods(["GET"])
def get_dashboard(request):

    merchant = request.GET.get("merchant_id")

    shipments = Shipment.objects.filter(

        merchant_id=merchant

    ).order_by("-created_at")[:5]

    tracking = Tracking.objects.filter(

        shipment__merchant_id=merchant

    ).order_by("-created_at")[:5]

    return JsonResponse({

        "stats":{

            "total":Shipment.objects.filter(
                merchant_id=merchant
            ).count()

        },

        "recent_shipments":ShipmentSerializer.serialize_many(shipments),

        "recent_tracking":TrackingSerializer.serialize_many(tracking)

    })

@require_http_methods(["GET"])
def recent_activity(request):

    merchant = request.GET.get("merchant_id")

    tracking = Tracking.objects.filter(

        shipment__merchant_id=merchant

    ).order_by("-created_at")[:10]

    return JsonResponse(

        TrackingSerializer.serialize_many(tracking),

        safe=False

    )

@require_http_methods(["GET"])
def get_invoices(request):

    merchant=request.GET.get("merchant_id")

    invoices=Invoice.objects.filter(
        merchant_id=merchant
    )

    return JsonResponse(

        InvoiceSerializer.serialize_many(invoices),

        safe=False

    )

@require_http_methods(["GET"])
def get_invoice(request,id):

    invoice=get_object_or_404(

        Invoice,

        id=id

    )

    return JsonResponse(

        InvoiceSerializer.serialize(invoice)

    )