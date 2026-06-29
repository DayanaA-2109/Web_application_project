from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.http import JsonResponse
import json


# Your existing get_users function
def get_users(request):
    users = User.objects.all()

    data = []
    for user in users:
        data.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role,
            "address": user.address,
            "city": user.city,
            "pincode": user.pincode,
            "is_active": user.is_active,
        })

    return JsonResponse(data, safe=False)


# Display all user
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'user': users})


# Add User
def add_user(request):
    if request.method == "POST":
        User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            phone=request.POST['phone'],
            role=request.POST['role'],
            address=request.POST['address'],
            city=request.POST['city'],
            pincode=request.POST['pincode']
        )
        return redirect('user_list')

    return render(request, 'user/add_user.html')


# Update User
def update_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.phone = request.POST['phone']
        user.role = request.POST['role']
        user.address = request.POST['address']
        user.city = request.POST['city']
        user.pincode = request.POST['pincode']
        user.save()

        return redirect('user_list')

    return render(request, 'user/update_user.html', {'user': user})


# Delete User
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('user_list')


# ============ ADD THESE NEW FUNCTIONS ============

# Get data from all three tables
def get_all_data(request):
    try:
        # Get all user
        users = User.objects.all()

        users_data = []
        for user in users:
            users_data.append({
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "phone": user.phone,
                "role": user.role,
                "address": user.address,
                "city": user.city,
                "pincode": user.pincode,
                "is_active": user.is_active,
            })

        # Get shipments data (if delivery app exists)
        shipments_data = []
        try:
            from delivery.models import Shipment
            shipments = Shipment.objects.all()
            for shipment in shipments:
                shipments_data.append({
                    "id": shipment.id,
                    "tracking_number": getattr(shipment, 'tracking_number', None),
                    "status": getattr(shipment, 'status', None),
                    "created_at": getattr(shipment, 'created_at', None),
                })
        except ImportError:
            shipments_data = "Shipment model not found"

        # Get tracking data (if tracking app exists)
        tracking_data = []
        try:
            from tracking.models import Tracking
            trackings = Tracking.objects.all()
            for tracking in trackings:
                tracking_data.append({
                    "id": tracking.id,
                    "location": getattr(tracking, 'location', None),
                    "status": getattr(tracking, 'status', None),
                    "timestamp": getattr(tracking, 'timestamp', None),
                })
        except ImportError:
            tracking_data = "Tracking model not found"

        response_data = {
            "user": users_data,
            "shipments": shipments_data,
            "trackings": tracking_data,
            "total_users": len(users_data),
            "total_shipments": len(shipments_data) if isinstance(shipments_data, list) else 0,
            "total_trackings": len(tracking_data) if isinstance(tracking_data, list) else 0
        }

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# Get specific user with their shipments
def get_user_with_details(request, user_id):
    try:
        user = User.objects.get(id=user_id)

        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role,
            "address": user.address,
            "city": user.city,
            "pincode": user.pincode,
            "is_active": user.is_active,
        }

        # Get shipments for this user
        shipments_data = []
        try:
            from delivery.models import Shipment
            shipments = Shipment.objects.filter(user_id=user_id)
            for shipment in shipments:
                shipments_data.append({
                    "id": shipment.id,
                    "tracking_number": getattr(shipment, 'tracking_number', None),
                    "status": getattr(shipment, 'status', None),
                    "created_at": getattr(shipment, 'created_at', None),
                })
        except ImportError:
            shipments_data = "Shipment model not found"

        response_data = {
            "user": user_data,
            "shipments": shipments_data
        }

        return JsonResponse(response_data)

    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)