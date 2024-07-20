from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', comenzar, name='comenzar'),
    path('vuelos/', vuelos, name="vuelos"),
    path('hoteles/', hoteles, name="hoteles"),
    path('traslados/', traslados, name="traslados"),
    path('acerca/', acerca, name="acerca"),

    #____ Formularios
    path('vueloForm/', vueloForm, name="vueloForm"),
    path('vueloUpdate/<id_vuelo>/', vueloUpdate, name="vueloUpdate"),
    path('vueloDelete/<id_vuelo>/', vueloDelete, name="vueloDelete"),

    path('hotelForm/', hotelForm, name="hotelForm"),
    path('hotelUpdate/<id_hotel>/', hotelUpdate, name="hotelUpdate"),
    path('hotelDelete/<id_hotel>/', hotelDelete, name="hotelDelete"),

    path('trasladoForm/', trasladoForm, name="trasladoForm"),
    path('trasladoUpdate/<id_traslado>/', trasladoUpdate, name="trasladoUpdate"),
    path('trasladoDelete/<id_traslado>/', trasladoDelete, name="trasladoDelete"),

    path('alquilerautos/', AlquilerautoList.as_view(), name="alquilerautos"),    
    path('alquilerautoCreate/', AlquilerautoCreate.as_view(), name="alquilerautoCreate"), 
    path('alquilerautoUpdate/<int:pk>/', AlquilerautoUpdate.as_view(), name="alquilerautoUpdate"), 
    path('alquilerautoDelete/<int:pk>/', AlquilerautoDelete.as_view(), name="alquilerautoDelete"), 

    path('buscarVuelos/', buscarVuelos, name="buscarVuelos"),
    path('encontrarVuelos/', encontrarVuelos, name="encontrarVuelos"),

    #-- Login,  Logout y Registration
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="misrubros/logout.html"), name="logout"),
    path('registro/', register, name="registro"),

    #-- Edición de Perfil y Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]