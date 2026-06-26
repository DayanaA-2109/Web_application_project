from django.shortcuts import render, redirect
from .models import User


def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            User.objects.get(email=email, password=password)
            return redirect('/home/')
        except User.DoesNotExist:
            return render(request, "login.html",
                          {"error": "Invalid Email or Password"})

    return render(request, "login.html")


def register(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            return render(request, "register.html",
                          {"error": "Email already exists"})

        User.objects.create(
            email=email,
            
            password=password
        )

        return redirect('/')

    return render(request, "register.html")


def home(request):
    return render(request, "home.html")