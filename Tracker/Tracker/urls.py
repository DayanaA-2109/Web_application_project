from django.contrib import admin
<<<<<<< HEAD
from django.urls import path,include

urlpatterns=[

    path('admin/',admin.site.urls),

    path('',include('delivery.urls')),

=======
from django.urls import path, include
from django.shortcuts import redirect
from . import views


def home(request):
    return redirect("dashboard_page")


urlpatterns = [

    path("admin/", admin.site.urls),

    # Existing home page
    path("", home, name="home"),

    # Existing pages (friend's code)
    path("dashboard-page/", views.dashboard_page, name="dashboard_page"),
    path("add-shipment/", views.add_shipment_page, name="add_shipment_page"),
    path("test/", views.api_test, name="api_test"),

    # YOUR E-COMMERCE BACKEND
    path("", include("e_commerce.urls")),

>>>>>>> 2241d53179dc078d5f6e15e5593825ce740de3d9
]