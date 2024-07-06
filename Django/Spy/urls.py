from django.urls import path
from Spy import views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('productos/ ', views.productos, name="productos"),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('inicioSesion/', views.inicioSesion, name='inicioSesion'), 
    path('registro/', views.registro, name='registro'),
    
   
]
