from django.urls import path
from . import views

urlpatterns = [
    path("read/", views.get_users, name="get_users"),
    path("all-data/", views.get_all_data, name="get_all_data"),  # New endpoint
    path("user-details/<int:user_id>/", views.get_user_with_details, name="user_details"),
]