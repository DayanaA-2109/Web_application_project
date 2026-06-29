from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import redirect


def home(request):
    return redirect("dashboard_page")


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Home
    path("", home, name="home"),

    # Existing pages (friend's code)
    path("dashboard-page/", views.dashboard_page, name="dashboard_page"),
    path("add-shipment/", views.add_shipment_page, name="add_shipment_page"),
    path("test/", views.api_test, name="api_test"),

    # E-COMMERCE API - YOUR REACT DASHBOARD
    # Using /api/ prefix to avoid conflicts
    path("api/", include("e_commerce.urls")),

    # LEADER APP - Friend's dashboards (admin, user, agent, merchant)
    path("", include("leader.urls")),

    # DELIVERY APP - Friend's delivery dashboard
    path("delivery/", include("delivery.urls")),
]