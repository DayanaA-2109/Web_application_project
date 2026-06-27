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

<<<<<<< HEAD
<<<<<<< HEAD
    # PAGES
    path('dashboard-page/', views.dashboard_page, name='dashboard_page'),
    path('add-shipment/', views.add_shipment_page, name='add_shipment_page'),
    path('test/', views.api_test, name='api_test'),
]
=======
]
>>>>>>> 3ead47315f72f376940dd63318e66f513808e327
=======
>>>>>>> 2241d53179dc078d5f6e15e5593825ce740de3d9
]
>>>>>>> 68e0586de8082010317c5626b64a1febb20617fd
