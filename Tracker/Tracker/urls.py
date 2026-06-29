from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import redirect


def home(request):
    return redirect("dashboard_page")

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("dashboard-page/", views.dashboard_page, name="dashboard_page"),
    path("login/", views.login_user, name="login_user"),   # <-- ADD THIS
    path("add-shipment/", views.add_shipment_page, name="add_shipment_page"),
    path("test/", views.api_test, name="api_test"),

    path("api/", include("e_commerce.urls")),


    # LEADER APP - Friend's dashboards (admin, user, agent, merchant)
    path("", include("leader.urls")),

    
    path("delivery/", include("delivery.urls")),

    path("", include("delivery.urls")),
>>>>>>> 647ae5b60c5123c96224d5908e57ac39b377b050
]