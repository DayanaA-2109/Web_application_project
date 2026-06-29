from django.urls import path
from . import views

urlpatterns = [

    # TEST
    path("test/", views.api_test, name="api_test"),

    # USERS
    path("user/", views.get_users, name="get_users"),
    path("user/<int:user_id>/", views.get_user, name="get_user"),
    path("merchants/", views.get_merchants, name="get_merchants"),
    path("merchant/<int:merchant_id>/", views.merchant_profile, name="merchant_profile"),
    path("merchant/<int:merchant_id>/update/", views.update_profile, name="update_profile"),

    # SHIPMENTS
    path("shipments/", views.get_shipments, name="get_shipments"),
    path("shipments/create/", views.create_shipment, name="create_shipment"),
    path("shipments/<str:awb>/", views.get_shipment, name="get_shipment"),
    path("shipments/<str:awb>/update/", views.update_shipment, name="update_shipment"),
    path("shipments/<str:awb>/delete/", views.delete_shipment, name="delete_shipment"),

    # TRACKING
    path("track/<str:awb>/", views.track_shipment, name="track_shipment"),

    # DASHBOARD
    path("stats/", views.get_stats, name="get_stats"),
    path("dashboard/", views.get_dashboard, name="get_dashboard"),
    path("recent-activity/", views.recent_activity, name="recent_activity"),

    # API KEY
    path("api-key/generate/", views.generate_api_key, name="generate_api_key"),

    # INVOICES
    path("invoices/", views.get_invoices, name="get_invoices"),
    path("invoices/<int:id>/", views.get_invoice, name="get_invoice"),
]