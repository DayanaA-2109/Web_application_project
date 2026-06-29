from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.http import JsonResponse
# Import your other models
from delivery.models import Shipment
from tracking.models import Tracking



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


# New view to get all data from three tables
def get_all_data(request):
    # Get all user
    users = User.objects.all()

    # Get all shipments (assuming you have a Shipment model)
    shipments = Shipment.objects.all()  # Adjust model name if different

    # Get all tracking records
    trackings = Tracking.objects.all()  # Adjust model name if different

    # Prepare user data
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

    # Prepare shipments data (adjust fields based on your Shipment model)
    shipments_data = []
    for shipment in shipments:
        shipments_data.append({
            "id": shipment.id,
            "tracking_number": shipment.tracking_number,  # Adjust field names
            "user": shipment.user.id if hasattr(shipment, 'user') else None,
            "status": shipment.status,  # Adjust field names
            "created_at": shipment.created_at,  # Adjust field names
            # Add other fields as needed
        })

    # Prepare tracking data (adjust fields based on your Tracking model)
    tracking_data = []
    for tracking in trackings:
        tracking_data.append({
            "id": tracking.id,
            "shipment": tracking.shipment.id if hasattr(tracking, 'shipment') else None,
            "location": tracking.location,  # Adjust field names
            "status": tracking.status,  # Adjust field names
            "timestamp": tracking.timestamp,  # Adjust field names
            # Add other fields as needed
        })

    # Combine all data
    response_data = {
        "user": users_data,
        "shipments": shipments_data,
        "trackings": tracking_data,
        "total_users": len(users_data),
        "total_shipments": len(shipments_data),
        "total_trackings": len(tracking_data)
    }

    return JsonResponse(response_data, safe=False)