from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sitemap', views.sitemap, name="sitemap"),
    path('about', views.about, name="about"),
    path('search', views.search, name="search"),
    path('train_between_stations', views.train_between_stations, name="train_between_stations"),
    path('train_info', views.train_info, name="train_info"),
    path('user_home', views.user_home, name="user_home"),
    path('user_info', views.user_info, name="user_info"),
]
