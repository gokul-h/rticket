from django.urls import path
from . import views

urlpatterns = [
    path('', views.pre_checkout, name='pre_checkout'),
    path('process', views.checkout_process, name='checkout_process'),
    path('history', views.history, name='order_history'),
]
