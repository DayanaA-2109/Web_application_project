from django.shortcuts import render, redirect
from .models import Parcel


# ==========================
# DISPLAY ALL PARCELS
# ==========================

def parcel_list(request):

    parcels = Parcel.objects.all()

    return render(
        request,
        'e-commerce/parcel_list.html',
        {'parcels': parcels}
    )


# ==========================
# ADD PARCEL
# ==========================

def addParcel(request):

    if request.method == "POST":

        Parcel.objects.create(
            tracking_id=request.POST['tracking_id'],
            parcel_type=request.POST['parcel_type'],

            sender_name=request.POST['sender_name'],
            sender_phone=request.POST['sender_phone'],

            receiver_name=request.POST['receiver_name'],
            receiver_phone=request.POST['receiver_phone'],

            product_name=request.POST.get('product_name'),

            weight=request.POST['weight'],

            booking_date=request.POST['booking_date'],

            current_status=request.POST['current_status']
        )

        return redirect('/e-commerce/e-commerce-list/')

    return render(
        request,
        'e-commerce/addParcel.html'
    )


# ==========================
# EDIT PARCEL PAGE
# ==========================

def editParcel(request, parcel_id):

    parcel = Parcel.objects.get(
        parcel_id=parcel_id
    )

    return render(
        request,
        'e-commerce/editParcel.html',
        {'e-commerce': parcel}
    )


# ==========================
# UPDATE PARCEL
# ==========================
def updateParcel(request, parcel_id):

    if request.method == "POST":

        parcel = Parcel.objects.get(parcel_id=parcel_id)

        parcel.tracking_id = request.POST['tracking_id']
        parcel.parcel_type = request.POST['parcel_type']

        parcel.sender_name = request.POST['sender_name']
        parcel.sender_phone = request.POST['sender_phone']

        parcel.receiver_name = request.POST['receiver_name']
        parcel.receiver_phone = request.POST['receiver_phone']

        parcel.product_name = request.POST['product_name']
        parcel.weight = request.POST['weight']

        parcel.current_status = request.POST['current_status']

        # DO NOT TOUCH booking_date

        parcel.save()

        return redirect('/e-commerce/e-commerce-list/')


# ==========================
# DELETE PARCEL
# ==========================

def deleteParcel(request, parcel_id):

    parcel = Parcel.objects.get(
        parcel_id=parcel_id
    )

    parcel.delete()

    return redirect('/e-commerce/e-commerce-list/')