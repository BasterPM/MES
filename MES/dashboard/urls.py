from django.urls import path
from dashboard.views.check_role_views import dashboard_view
from dashboard.views.manager.view import *

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('add_order', add_order_view, name='add_order'),
    path('add_client', add_client_view, name='add_client'),
    path('all_order', all_order_view, name='all_order'),
    path('order/<int:id>', order_view, name='order'),
    ]
