# e_commerce/views.py

import secrets
import json
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import User, Shipment, Tracking
from .serializers import (
    UserSerializer, ShipmentSerializer, TrackingSerializer
)


# ============================================
# 1. TEST ENDPOINT
# ============================================

def api_test(request):
    return JsonResponse({
        'status': 'success',
        'message': 'E-commerce API is running!',
        'version': '1.0',
        'endpoints': {
            'test': '/api/test/',
            'users': '/api/users/',
            'merchants': '/api/merchants/',
            'shipments': '/api/shipments/',
            'shipment_detail': '/api/shipments/<awb>/',
            'create_shipment': '/api/shipments/create/',
            'update_shipment': '/api/shipments/<awb>/update/',
            'track': '/api/track/<awb>/',
            'stats': '/api/stats/?merchant_id=1',
            'dashboard': '/api/dashboard/?merchant_id=1',
            'api_key': '/api/api-keys/generate/',
        }
    })


# ============================================
# 2. USERS
# ============================================

def get_users(request):
    users = User.objects.filter(is_active=True)
    data = UserSerializer.serialize_many(users)
    return JsonResponse(data, safe=False)


def get_merchants(request):
    merchants = User.objects.filter(role='merchant', is_active=True)
    data = UserSerializer.serialize_many(merchants)
    return JsonResponse(data, safe=False)


def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    data = UserSerializer.serialize(user)
    return JsonResponse(data)


# ============================================
# 3. SHIPMENTS
# ============================================

def get_shipments(request):
    merchant_id = request.GET.get('merchant_id')
    status_filter = request.GET.get('status')

    shipments = Shipment.objects.all()

    if merchant_id:
        shipments = shipments.filter(merchant_id=merchant_id)
    if status_filter:
        shipments = shipments.filter(status=status_filter)

    shipments = shipments.order_by('-created_at')
    data = ShipmentSerializer.serialize_many(shipments)
    return JsonResponse(data, safe=False)


def get_shipment(request, awb_number):
    shipment = get_object_or_404(Shipment, awb_number=awb_number)
    data = ShipmentSerializer.serialize(shipment)
    return JsonResponse(data)


@csrf_exempt
@require_http_methods(["POST"])
def create_shipment(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    required_fields = ['merchant_id', 'receiver_name', 'receiver_phone',
                       'receiver_address', 'receiver_city', 'receiver_pincode', 'weight']

    for field in required_fields:
        if field not in data:
            return JsonResponse({'error': f'{field} is required'}, status=400)

    awb = f"SH-{datetime.now().strftime('%y%m%d')}-{secrets.token_hex(4).upper()}"

    shipment = Shipment.objects.create(
        awb_number=awb,
        merchant_id=data['merchant_id'],
        receiver_name=data['receiver_name'],
        receiver_phone=data['receiver_phone'],
        receiver_address=data['receiver_address'],
        receiver_city=data['receiver_city'],
        receiver_pincode=data['receiver_pincode'],
        weight=data['weight'],
        cod_amount=data.get('cod_amount', 0),
        order_id=data.get('order_id'),
        expected_delivery=data.get('expected_delivery'),
        status='pending'
    )

    Tracking.objects.create(
        shipment=shipment,
        status='Order Placed',
        location=data['receiver_city'],
        remarks='Shipment created successfully'
    )

    return JsonResponse({
        'success': True,
        'message': 'Shipment created successfully',
        'awb_number': awb,
        'shipment': ShipmentSerializer.serialize(shipment)
    }, status=201)


@csrf_exempt
@require_http_methods(["PUT"])
def update_shipment(request, awb_number):
    shipment = get_object_or_404(Shipment, awb_number=awb_number)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    allowed_fields = ['receiver_name', 'receiver_phone', 'receiver_address',
                      'receiver_city', 'receiver_pincode', 'weight', 'cod_amount']

    for field in allowed_fields:
        if field in data:
            setattr(shipment, field, data[field])

    if 'status' in data:
        valid_statuses = ['pending', 'picked_up', 'in_transit', 'out_for_delivery', 'delivered', 'failed']
        if data['status'] in valid_statuses:
            shipment.status = data['status']

            if data['status'] == 'delivered':
                shipment.delivered_at = datetime.now()

            Tracking.objects.create(
                shipment=shipment,
                status=data['status'].replace('_', ' ').title(),
                location=data.get('location', shipment.receiver_city),
                remarks=data.get('remarks', f'Status updated to {data["status"]}')
            )

    shipment.save()
    return JsonResponse({
        'success': True,
        'message': 'Shipment updated successfully',
        'shipment': ShipmentSerializer.serialize(shipment)
    })


# ============================================
# 4. TRACKING
# ============================================

def track_shipment(request, awb_number):
    shipment = get_object_or_404(Shipment, awb_number=awb_number)
    tracking_entries = Tracking.objects.filter(shipment=shipment).order_by('created_at')

    return JsonResponse({
        'awb_number': shipment.awb_number,
        'current_status': shipment.status,
        'receiver_name': shipment.receiver_name,
        'expected_delivery': shipment.expected_delivery,
        'delivered_at': shipment.delivered_at,
        'timeline': TrackingSerializer.serialize_many(tracking_entries)
    })


# ============================================
# 5. API KEYS
# ============================================

@csrf_exempt
@require_http_methods(["POST"])
def generate_api_key(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    merchant_id = data.get('merchant_id')
    key_name = data.get('key_name', 'Default API Key')

    if not merchant_id:
        return JsonResponse({'error': 'merchant_id required'}, status=400)

    try:
        merchant = User.objects.get(id=merchant_id, role='merchant')
    except User.DoesNotExist:
        return JsonResponse({'error': 'Merchant not found'}, status=404)

    api_key = f"sk_{secrets.token_hex(32)}"

    return JsonResponse({
        'success': True,
        'api_key': api_key,
        'key_name': key_name,
        'merchant_id': merchant_id,
        'merchant_name': merchant.name,
        'instructions': 'Use this key in X-API-Key header',
        'example': f"curl -H 'X-API-Key: {api_key}' http://localhost:8000/api/shipments/"
    })


# ============================================
# 6. DASHBOARD
# ============================================

def get_stats(request):
    merchant_id = request.GET.get('merchant_id')

    shipments = Shipment.objects.all()
    if merchant_id:
        shipments = shipments.filter(merchant_id=merchant_id)

    total = shipments.count()
    delivered = shipments.filter(status='delivered').count()
    in_transit = shipments.filter(status__in=['picked_up', 'in_transit', 'out_for_delivery']).count()
    pending = shipments.filter(status='pending').count()
    failed = shipments.filter(status='failed').count()

    return JsonResponse({
        'total_shipments': total,
        'delivered': delivered,
        'in_transit': in_transit,
        'pending': pending,
        'failed': failed,
        'delivery_rate': round((delivered / total * 100) if total > 0 else 0, 1)
    })


def get_dashboard(request):
    merchant_id = request.GET.get('merchant_id')

    if not merchant_id:
        return JsonResponse({'error': 'merchant_id required'}, status=400)

    shipments = Shipment.objects.filter(merchant_id=merchant_id).order_by('-created_at')[:10]
    recent_tracking = Tracking.objects.filter(
        shipment__merchant_id=merchant_id
    ).order_by('-created_at')[:5]

    all_shipments = Shipment.objects.filter(merchant_id=merchant_id)
    total = all_shipments.count()
    delivered = all_shipments.filter(status='delivered').count()

    return JsonResponse({
        'stats': {
            'total_shipments': total,
            'delivered': delivered,
            'in_transit': all_shipments.filter(status__in=['picked_up', 'in_transit', 'out_for_delivery']).count(),
            'pending': all_shipments.filter(status='pending').count(),
            'failed': all_shipments.filter(status='failed').count(),
            'delivery_rate': round((delivered / total * 100) if total > 0 else 0, 1)
        },
        'recent_shipments': ShipmentSerializer.serialize_many(shipments),
        'recent_activity': TrackingSerializer.serialize_many(recent_tracking),
        'last_updated': datetime.now().isoformat()
    })
# e_commerce/views.py

def dashboard_page(request):
    return render(request, 'ecommerce_dashboard.html')