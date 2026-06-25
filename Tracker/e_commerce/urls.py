# e_commerce/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Test
    path('test/', views.api_test, name='api_test'),

    # Users
    path('users/', views.get_users, name='get_users'),
    path('users/<int:user_id>/', views.get_user, name='get_user'),
    path('merchants/', views.get_merchants, name='get_merchants'),

    # Shipments
    path('shipments/', views.get_shipments, name='get_shipments'),
    path('shipments/<str:awb_number>/', views.get_shipment, name='get_shipment'),
    path('shipments/create/', views.create_shipment, name='create_shipment'),
    path('shipments/<str:awb_number>/update/', views.update_shipment, name='update_shipment'),

    # Tracking
    path('track/<str:awb_number>/', views.track_shipment, name='track_shipment'),

    # API Keys
    path('api-keys/generate/', views.generate_api_key, name='generate_api_key'),

    # Dashboard
    path('stats/', views.get_stats, name='get_stats'),
    path('dashboard/', views.get_dashboard, name='get_dashboard'),
path('dashboard-page/', views.dashboard_page, name='dashboard_page'),
]