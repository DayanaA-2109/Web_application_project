from django.shortcuts import render, redirect, get_object_or_404
from .models import Delivery
from .forms import DeliveryForm


def home(request):

    deliveries = Delivery.objects.all()

    return render(request,'delivery/home.html',{
        'deliveries':deliveries
    })


def add_delivery(request):

    if request.method=="POST":

        form=DeliveryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form=DeliveryForm()

    return render(request,'delivery/add_delivery.html',{
        'form':form
    })


def update_delivery(request,id):

    delivery=get_object_or_404(Delivery,id=id)

    if request.method=="POST":

        form=DeliveryForm(request.POST,instance=delivery)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:

        form=DeliveryForm(instance=delivery)

    return render(request,'delivery/update_delivery.html',{
        'form':form
    })


def delete_delivery(request,id):

    delivery=get_object_or_404(Delivery,id=id)

    delivery.delete()

    return redirect('home')