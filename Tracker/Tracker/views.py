from django.http import HttpResponse
from django.shortcuts import render

# DASHBOARD PAGE (HTML)
def dashboard_page(request):
    return render(request, 'index.html')

# ADD SHIPMENT PAGE
def add_shipment_page(request):
    return HttpResponse("<h1>Add Shipment Page</h1>")

# TEST API
def api_test(request):
    return HttpResponse("<h1>API Test Working</h1>")


from django.shortcuts import render

def login_user(request):

    if request.method == "POST":

        role = request.POST.get("role")

        context = {

            "name": request.POST.get("name"),

            "email": request.POST.get("email"),

            "phone": request.POST.get("phone")

        }

        if role == "Admin":
            return render(request, "admin_dashboard.html", context)

        elif role == "User":
            return render(request, "user_dashboard.html", context)

        elif role == "Agent":
            return render(request, "agent_dashboard.html", context)

        elif role == "Merchant":
            return render(request, "merchant_dashboard.html", context)

    return render(request, "index.html")

