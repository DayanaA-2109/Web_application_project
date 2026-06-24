from django.shortcuts import render
from django.http import JsonResponse
from .models import Parcel
from django.views.decorators.csrf import csrf_exempt
import json


def parcel_list(request):
    parcels = Parcel.objects.all()

    return render(
        request,
        'parcel/parcel_list.html',
        {'parcels': parcels}
    )


def DisplayParcels(request):

    parcels = list(
        Parcel.objects.values()
    )

    return JsonResponse(
        parcels,
        safe=False
    )


@csrf_exempt
def insertParcel(request):

    if request.method == "POST":

        data = json.loads(request.body)

        Parcel.objects.create(
            tracking_id=data['tracking_id'],
            parcel_type=data['parcel_type'],
            sender_name=data['sender_name'],
            sender_phone=data['sender_phone'],
            receiver_name=data['receiver_name'],
            receiver_phone=data['receiver_phone'],
            product_name=data.get('product_name'),
            weight=data['weight'],
            booking_date=data['booking_date'],
            current_status=data['current_status']
        )

        return JsonResponse({
            "message": "Parcel Added Successfully"
        })


@csrf_exempt
def updateParcel(request, tracking_id):

    if request.method == "PUT":

        data = json.loads(request.body)

        try:

            parcel = Parcel.objects.get(
                tracking_id=tracking_id
            )

            parcel.parcel_type = data['parcel_type']
            parcel.sender_name = data['sender_name']
            parcel.sender_phone = data['sender_phone']
            parcel.receiver_name = data['receiver_name']
            parcel.receiver_phone = data['receiver_phone']
            parcel.product_name = data.get('product_name')
            parcel.weight = data['weight']
            parcel.current_status = data['current_status']

            parcel.save()

            return JsonResponse({
                "message": "Updated Successfully"
            })

        except Parcel.DoesNotExist:

            return JsonResponse({
                "error": "Parcel Not Found"
            })


@csrf_exempt
def deleteParcel(request, tracking_id):

    if request.method == "DELETE":

        try:

            parcel = Parcel.objects.get(
                tracking_id=tracking_id
            )

            parcel.delete()

            return JsonResponse({
                "message": "Deleted Successfully"
            })

        except Parcel.DoesNotExist:

            return JsonResponse({
                "error": "Parcel Not Found"
            })