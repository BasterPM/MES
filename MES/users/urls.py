from django.urls import path
from .views import start_page_view, register_view, logout_view

urlpatterns = [
    path('', start_page_view, name='start_page'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
