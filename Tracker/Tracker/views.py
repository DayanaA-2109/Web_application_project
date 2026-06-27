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