from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('quick_report/entrada', views.tela_entrada, name='tela_entrada'),
    path('quick_report/edicao', views.tela_edicao, name='tela_edicao'),
    path('quick_report/audio_to_text', views.audio_to_text, name='audio_to_text'),
]
