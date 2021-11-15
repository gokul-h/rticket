from django.urls import path
from . import views

urlpatterns = [
    # path('', views.checkout, name='checkout'),
    path('history', views.history, name='order_history'),
]
