from django.urls import path
from dashboard.views.views import dashboard_view, my_tasks_view
from dashboard.views.manager.view import *
from dashboard.views.head_of_production.view import *

manager_urls = [
    path('add_order', add_order_view, name='add_order'),
    path('add_client', add_client_view, name='add_client'),
    path('all_order', all_order_view, name='all_order'),
    path('order/<int:id>', order_view, name='order'),
    ]

head_of_production_urls = [
    path('add_product', add_product_view, name='add_product'),
    path('add_assembly', add_assembly_view, name='add_assembly'),
    path('add_own_product', add_own_product_view, name='add_own_product'),
    path('add_store_house_element', add_store_house_element_view, name='add_store_house_element'),
    path('add_task', add_task_view, name='add_task'),
    
    ]

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('tasks', my_tasks_view, name='tasks'),
    ] + manager_urls + head_of_production_urls
