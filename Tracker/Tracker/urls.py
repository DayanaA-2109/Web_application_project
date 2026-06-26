from django.contrib import admin
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

<<<<<<< HEAD
    # PAGES
    path('dashboard-page/', views.dashboard_page, name='dashboard_page'),
    path('add-shipment/', views.add_shipment_page, name='add_shipment_page'),
    path('test/', views.api_test, name='api_test'),
]
=======
]
>>>>>>> 3ead47315f72f376940dd63318e66f513808e327
