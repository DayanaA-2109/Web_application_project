# e_commerce/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db import connection
import secrets
import json
from datetime import datetime

from .models import User, Shipment, Tracking
from .serializers import (
    UserSerializer, ShipmentSerializer, TrackingSerializer
)


# ============================================
# PAGE VIEWS
# ============================================

def dashboard_page(request):
    """Serve the E-commerce Dashboard HTML page"""
    return render(request, 'ecommerce_dashboard.html')


def add_shipment_page(request):
    """Serve the Add Shipment HTML page"""
    return render(request, 'addshipment.html')


# ============================================
# API: FIX MERCHANT IDS
# ============================================

@csrf_exempt
def fix_merchant_ids(request):
    """Fix merchant_id for all shipments (set to 1)"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                           UPDATE shipments
                           SET merchant_id = 1
                           WHERE merchant_id IS NULL
                              OR merchant_id = 0
                           """)
            cursor.execute("SELECT ROW_COUNT()")
            updated_count = cursor.fetchone()[0]

        return JsonResponse({
            'success': True,
            'message': f'✅ Fixed {updated_count} shipment(s)',
            'updated_count': updated_count,
            'instructions': 'Refresh your dashboard to see shipments!'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


# ============================================
# API: TEST ENDPOINT
# ============================================

def api_test(request):
    """Test API endpoint"""
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
            'delete_shipment': '/api/shipments/<awb>/delete/',
            'track': '/api/track/<awb>/',
            'stats': '/api/stats/?merchant_id=1',
            'dashboard': '/api/dashboard/?merchant_id=1',
            'api_key': '/api/api-keys/generate/',
            'fix_merchant_ids': '/api/fix-merchant-ids/',
            'recent_activity': '/api/recent-activity/?merchant_id=1',
            'add_shipment': '/api/add-shipment/',
        }
    })


# ============================================
# API: USERS
# ============================================

def get_users(request):
    """Get all active users"""
    users = User.objects.filter(is_active=True)
    data = UserSerializer.serialize_many(users)
    return JsonResponse(data, safe=False)


def get_merchants(request):
    """Get all merchants"""
    merchants = User.objects.filter(role='merchant', is_active=True)
    data = UserSerializer.serialize_many(merchants)
    return JsonResponse(data, safe=False)


def get_user(request, user_id):
    """Get specific user by ID"""
    user = get_object_or_404(User, id=user_id)
    data = UserSerializer.serialize(user)
    return JsonResponse(data)


# ============================================
# API: SHIPMENTS - FULL CRUD
# ============================================

def get_shipments(request):
    """GET all shipments (READ)"""
    merchant_id = request.GET.get('merchant_id')
    status_filter = request.GET.get('status')
    search = request.GET.get('search')

    shipments = Shipment.objects.all()

    if merchant_id:
        shipments = shipments.filter(merchant_id=merchant_id)
    if status_filter:
        shipments = shipments.filter(status=status_filter)
    if search:
        shipments = shipments.filter(awb_number__icontains=search)

    shipments = shipments.order_by('-created_at')
    data = ShipmentSerializer.serialize_many(shipments)
    return JsonResponse(data, safe=False)


def get_shipment(request, awb_number):
    """GET single shipment by AWB (READ)"""
    shipment = get_object_or_404(Shipment, awb_number=awb_number)
    data = ShipmentSerializer.serialize(shipment)
    return JsonResponse(data)



@require_http_methods(["POST"])
@csrf_exempt
def create_shipment(request):
    """CREATE a new shipment using JSON (for Postman/API)"""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    required_fields = ['merchant_id', 'receiver_name', 'receiver_phone',
                       'receiver_address', 'receiver_city', 'receiver_pincode', 'weight']

    for field in required_fields:
        if field not in data or not data[field]:
            return JsonResponse({'error': f'{field} is required'}, status=400)

    try:
        # Generate AWB number
        awb = f"SH-{datetime.now().strftime('%y%m%d')}-{secrets.token_hex(4).upper()}"

        # Create shipment
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
            order_id=data.get('order_id', ''),
            expected_delivery=data.get('expected_delivery', None),
            status='pending'
        )

        # Create tracking entry
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

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def create_shipment(request):
    """CREATE shipment from HTML form"""

    if request.method == 'POST':

        merchant_id = request.POST.get('merchant_id', 1)

        receiver_name = request.POST.get('receiver_name')
        receiver_phone = request.POST.get('receiver_phone')
        receiver_address = request.POST.get('receiver_address')
        receiver_city = request.POST.get('receiver_city')
        receiver_pincode = request.POST.get('receiver_pincode')

        weight = request.POST.get('weight')
        cod_amount = request.POST.get('cod_amount', 0)

        order_id = request.POST.get('order_id', '')
        expected_delivery = request.POST.get('expected_delivery')

        try:

            awb = f"SH-{datetime.now().strftime('%y%m%d')}-{secrets.token_hex(4).upper()}"

            shipment = Shipment.objects.create(
                awb_number=awb,
                merchant_id=merchant_id,
                receiver_name=receiver_name,
                receiver_phone=receiver_phone,
                receiver_address=receiver_address,
                receiver_city=receiver_city,
                receiver_pincode=receiver_pincode,
                weight=weight,
                cod_amount=cod_amount,
                order_id=order_id,
                expected_delivery=expected_delivery if expected_delivery else None,
                status='pending'
            )

            Tracking.objects.create(
                shipment=shipment,
                status='Order Placed',
                location=receiver_city,
                remarks='Shipment created successfully'
            )

            return render(request, 'addshipment.html', {
                'success': True,
                'awb_number': awb
            })

        except Exception as e:

            return render(request, 'addshipment.html', {
                'error': str(e)
            })

    return render(request, 'addshipment.html')



@csrf_exempt
@require_http_methods(["PUT"])
def update_shipment(request, awb_number):
    """UPDATE a shipment"""
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


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_shipment(request, awb_number):
    """DELETE a shipment (only if pending)"""
    shipment = get_object_or_404(Shipment, awb_number=awb_number)

    if shipment.status != 'pending':
        return JsonResponse({
            'error': 'Cannot delete shipment that is in progress'
        }, status=400)

    shipment.delete()
    return JsonResponse({
        'success': True,
        'message': f'Shipment {awb_number} deleted successfully'
    })


# ============================================
# API: TRACKING
# ============================================

def track_shipment(request, awb_number):
    """Get complete tracking timeline for a shipment"""
    shipment = get_object_or_404(Shipment, awb_number=awb_number)
    tracking_entries = Tracking.objects.filter(shipment=shipment).order_by('created_at')

    return JsonResponse({
        'awb_number': shipment.awb_number,
        'current_status': shipment.status,
        'receiver_name': shipment.receiver_name,
        'receiver_phone': shipment.receiver_phone,
        'receiver_address': shipment.receiver_address,
        'receiver_city': shipment.receiver_city,
        'expected_delivery': shipment.expected_delivery,
        'delivered_at': shipment.delivered_at,
        'timeline': TrackingSerializer.serialize_many(tracking_entries)
    })


def get_recent_activity(request):
    """Get recent activity (tracking history) for a merchant"""
    merchant_id = request.GET.get('merchant_id')

    if not merchant_id:
        return JsonResponse({'error': 'merchant_id required'}, status=400)

    recent_activity = Tracking.objects.filter(
        shipment__merchant_id=merchant_id
    ).select_related('shipment').order_by('-created_at')[:10]

    activity_data = []
    for track in recent_activity:
        activity_data.append({
            'id': track.id,
            'awb_number': track.shipment.awb_number,
            'status': track.status,
            'location': track.location,
            'remarks': track.remarks,
            'created_at': track.created_at,
            'receiver_name': track.shipment.receiver_name,
            'receiver_city': track.shipment.receiver_city
        })

    return JsonResponse({
        'success': True,
        'count': len(activity_data),
        'activity': activity_data
    })


# ============================================
# API: API KEYS
# ============================================

@csrf_exempt
@require_http_methods(["POST"])
def generate_api_key(request):
    """Generate unique API key for merchant"""
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
        'created_at': datetime.now().isoformat(),
        'instructions': 'Use this key in X-API-Key header'
    })


# ============================================
# API: DASHBOARD STATS
# ============================================

def get_stats(request):
    """Get statistics for merchant"""
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
    """Get complete dashboard data for merchant"""
    merchant_id = request.GET.get('merchant_id')

    if not merchant_id:
        return JsonResponse({'error': 'merchant_id required'}, status=400)

    # Recent shipments
    shipments = Shipment.objects.filter(
        merchant_id=merchant_id
    ).order_by('-created_at')[:10]

    # Recent activity
    recent_tracking = Tracking.objects.filter(
        shipment__merchant_id=merchant_id
    ).order_by('-created_at')[:5]

    # Stats
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
