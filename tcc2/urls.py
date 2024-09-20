from django.urls import path
from . import views

urlpatterns = [
    path('entrada', views.tela_entrada, name='tela_entrada'),
    path('edicao', views.tela_edicao, name='tela_edicao'),
]
