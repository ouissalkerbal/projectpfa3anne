# app/urls.py
from django.urls import path
from django.contrib import admin  # Import the admin object
from . import views

app_name = 'app'  # Specify the app_name matching the 'app' in MyProject/urls.py

urlpatterns = [
    path('', views.home, name='home'),
    path('custom_admin/', admin.site.urls),  # Use a different namespace for admin URLs
     path('service/commercial/', views.service_commercial, name='service_commercial'),
     path('service/atelier/', views.service_atelier, name='service_atelier'),  # Add this line
    path('purchase_order/<int:purchase_order_id>/', views.purchase_order_detail, name='purchase_order_detail'),
    path('bon_de_commande/', views.bon_de_commande, name='bon_de_commande'),
     path('notifications/', views.notifications_view, name='notifications'),
     path('save_message/', views.save_message, name='save_message'),
     path('fetch_messages/', views.fetch_messages, name='fetch_messages'),

]
