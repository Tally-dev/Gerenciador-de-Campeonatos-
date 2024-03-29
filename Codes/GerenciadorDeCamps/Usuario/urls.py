from modulefinder import packagePathMap
from re import template
from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='index'),
    ] 