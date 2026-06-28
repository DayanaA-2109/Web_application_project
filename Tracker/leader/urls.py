from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Delivery CRUD
    path('add/', views.add_delivery, name='add_delivery'),
    path('update/<int:id>/', views.update_delivery, name='update_delivery'),
    path('delete/<int:id>/', views.delete_delivery, name='delete_delivery'),

    # Login
    path('login-user/', views.login_user, name='login_user'),

    # Dashboards
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('agent-dashboard/', views.agent_dashboard, name='agent_dashboard'),
    path('merchant-dashboard/', views.merchant_dashboard, name='merchant_dashboard'),
    path('dashboard-page/', views.dashboard_page, name='dashboard_page')

]