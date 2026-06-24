from django.urls import path
from . import views

urlpatterns = [

    path(
        'parcel-list/',
        views.parcel_list,
        name='parcel_list'
    ),

    path(
        'addParcel/',
        views.addParcel,
        name='addParcel'
    ),

    path(
        'editParcel/<int:parcel_id>/',
        views.editParcel,
        name='editParcel'
    ),

    path(
        'updateParcel/<int:parcel_id>/',
        views.updateParcel,
        name='updateParcel'
    ),

    path(
        'deleteParcel/<int:parcel_id>/',
        views.deleteParcel,
        name='deleteParcel'
    ),
]