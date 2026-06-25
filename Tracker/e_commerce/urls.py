# e_commerce/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # PAGE VIEWS
    path('dashboard-page/', views.dashboard_page, name='dashboard_page'),
    path('add-shipment/', views.add_shipment_page, name='add_shipment_page'),

    # API ENDPOINTS
    path('test/', views.api_test, name='api_test'),
    path('users/', views.get_users, name='get_users'),
    path('users/<int:user_id>/', views.get_user, name='get_user'),
    path('merchants/', views.get_merchants, name='get_merchants'),

    # ✅ CREATE - Uses form data, no csrf_exempt needed in URL
    path('shipments/create/', views.create_shipment, name='create_shipment'),
    path('shipments/', views.get_shipments, name='get_shipments'),
    path('shipments/<str:awb_number>/', views.get_shipment, name='get_shipment'),

    path('track/<str:awb_number>/', views.track_shipment, name='track_shipment'),
    path('api-keys/generate/', views.generate_api_key, name='generate_api_key'),
    path('stats/', views.get_stats, name='get_stats'),
    path('dashboard/', views.get_dashboard, name='get_dashboard'),
    path('recent-activity/', views.get_recent_activity, name='recent_activity'),
    path('fix-merchant-ids/', views.fix_merchant_ids, name='fix_merchant_ids'),
path(
    'shipments/<str:awb_number>/update/',
    views.update_shipment,
    name='update_shipment'
),

path(
    'shipments/<str:awb_number>/delete/',
    views.delete_shipment,
    name='delete_shipment'
),


]