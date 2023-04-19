from modulefinder import packagePathMap
from re import template
from django.urls import path

from . import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('<int:campeonato_id>/', views.detail, name='detail'),
    path('excluir/<int:campeonato_id>/', views.excluir, name='excluir'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:campeonato_id>/', views.editar, name='editar'),
] 