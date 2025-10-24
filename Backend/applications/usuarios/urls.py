from django.urls import path
from .import views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('profile/', views.perfil_usuario, name='perfil'),
    path('google-login/', views.google_login, name='google_login'),
]