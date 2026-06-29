from django.urls import path
from . import views

urlpatterns=[

    path('',views.home,name='home'),

    path('add/',views.add_delivery,name='add_delivery'),

    path('update/<int:id>/',views.update_delivery,name='update_delivery'),

    path('delete/<int:id>/',views.delete_delivery,name='delete_delivery'),

]