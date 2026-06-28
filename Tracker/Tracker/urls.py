from django.contrib import admin
from django.urls import path,include
from . import views
from django.shortcuts import redirect

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

    # PAGES
    path('dashboard-page/', views.dashboard_page, name='dashboard_page'),
    path('add-shipment/', views.add_shipment_page, name='add_shipment_page'),
    path('test/', views.api_test, name='api_test'),
    path('admin/',admin.site.urls),

    path('',include('delivery.urls')),
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page
    path('', views.dashboard_page, name='home'),

    # Existing page
    path('dashboard-page/', views.dashboard_page, name='dashboard_page'),

    # Login
    path('login-user/', views.login_user, name='login_user'),
]
