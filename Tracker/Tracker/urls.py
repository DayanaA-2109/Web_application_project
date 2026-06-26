from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from . import views

# HOME FUNCTION
def home(request):
    return redirect('dashboard_page')

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME URL (FIX 404)
    path('', home, name='home'),

    # PAGES
    path('dashboard-page/', views.dashboard_page, name='dashboard_page'),
    path('add-shipment/', views.add_shipment_page, name='add_shipment_page'),
    path('test/', views.api_test, name='api_test'),
]