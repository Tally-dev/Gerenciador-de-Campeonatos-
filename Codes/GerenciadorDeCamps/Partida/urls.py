from modulefinder import packagePathMap
from re import template
from django.urls import path

from . import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('<int:partida_id>/', views.detail, name='detail'),
    path('excluir/<int:partida_id>/', views.excluir, name='excluir'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:partida_id>/', views.editar, name='editar'),
] 