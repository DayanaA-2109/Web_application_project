from django.urls import path
from . import views

urlpatterns = [

    # Display all parcels
    path('parcel-list/', views.parcel_list, name='parcel_list'),

    # Add Parcel
    path('addParcel/', views.addParcel, name='addParcel'),

    # Edit Parcel
    path('editParcel/<int:parcel_id>/', views.editParcel, name='editParcel'),

    # Delete Parcel
    path('deleteParcel/<int:parcel_id>/', views.deleteParcel, name='deleteParcel'),
]