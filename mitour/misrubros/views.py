from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def comenzar(request):
    return render(request, 'misrubros/index.html')

@login_required
def vuelos(request):
    contexto = {"vuelos": Vuelo.objects.all()}
    return render(request, "misrubros/vuelos.html", contexto)

@login_required
def hoteles(request):
    contexto = {"hoteles": Hotel.objects.all()}
    return render(request, "misrubros/hoteles.html", contexto)

@login_required
def traslados(request):
    contexto = {"traslados": Traslado.objects.all()}
    return render(request, "misrubros/traslados.html", contexto)


def acerca(request):
    return render(request, "misrubros/acerca.html")


#___ Formularios de Vuelos
@login_required
def vueloForm(request):
    if request.method == "POST":
        miForm = VueloForm(request.POST)
        if miForm.is_valid():
            v_nombre       = miForm.cleaned_data.get("nombre")
            v_numero       = miForm.cleaned_data.get("numero")
            v_origen       = miForm.cleaned_data.get("origen")
            v_destino      = miForm.cleaned_data.get("destino")
            v_fecha        = miForm.cleaned_data.get("fecha")
            v_hora         = miForm.cleaned_data.get("hora")
            v_fecha_compra = miForm.cleaned_data.get("fecha_compra")

            vuelo = Vuelo(nombre=v_nombre, numero=v_numero, origen=v_origen, destino=v_destino,
                          fecha=v_fecha, hora=v_hora, fecha_compra=v_fecha_compra)
            vuelo.save()
            contexto = {"vuelos": Vuelo.objects.all() }
            return render(request, "misrubros/vuelos.html", contexto)

    else:
        miForm = VueloForm()
    
    return render(request, "misrubros/vueloForm.html", {"form": miForm})

@login_required
def vueloUpdate(request, id_vuelo):
    vuelo = Vuelo.objects.get(id=id_vuelo)
    if request.method == "POST":
        miForm = VueloForm(request.POST)
        if miForm.is_valid():
            vuelo.nombre       = miForm.cleaned_data.get("nombre")
            vuelo.numero       = miForm.cleaned_data.get("numero") 
            vuelo.origen       = miForm.cleaned_data.get("origen")
            vuelo.destino      = miForm.cleaned_data.get("destino")
            vuelo.fecha        = miForm.cleaned_data.get("fecha")
            vuelo.hora         = miForm.cleaned_data.get("hora")
            vuelo.fecha_compra = miForm.cleaned_data.get("fecha_compra")
            vuelo.save()
            contexto = {"vuelos": Vuelo.objects.all() }
            return render(request, "misrubros/vuelos.html", contexto)       
    else:
        miForm = VueloForm(initial={"nombre": vuelo.nombre, "numero": vuelo.numero, "origen": vuelo.origen,
                           "destino": vuelo.destino, "fecha": vuelo.fecha, "hora": vuelo.hora,
                           "fecha_compra": vuelo.fecha_compra}) 
    
    return render(request, "misrubros/vueloForm.html", {"form": miForm})

def vueloDelete(request, id_vuelo):
    vuelo = Vuelo.objects.get(id=id_vuelo)
    vuelo.delete()
    contexto = {"vuelos": Vuelo.objects.all() }
    return render(request, "misrubros/vuelos.html", contexto)     


#___ Formularios de Hoteles
@login_required
def hotelForm(request):
    if request.method == "POST":
        miForm = HotelForm(request.POST)
        if miForm.is_valid():
            h_nombre         = miForm.cleaned_data.get("nombre")
            h_ciudad         = miForm.cleaned_data.get("ciudad")
            h_pais           = miForm.cleaned_data.get("pais")
            h_fecha_desde    = miForm.cleaned_data.get("fecha_desde")
            h_fecha_hasta    = miForm.cleaned_data.get("fecha_hasta")
            h_fecha_compra   = miForm.cleaned_data.get("fecha_compra")

            hotel = Hotel(nombre=h_nombre, ciudad=h_ciudad, pais=h_pais, fecha_desde=h_fecha_desde,
                          fecha_hasta=h_fecha_hasta, fecha_compra=h_fecha_compra)
            hotel.save()
            contexto = {"hoteles": Hotel.objects.all() }
            return render(request, "misrubros/hoteles.html", contexto)
    else:
        miForm = HotelForm()
    
    return render(request, "misrubros/hotelForm.html", {"form": miForm})

@login_required
def hotelUpdate(request, id_hotel):
    hotel = Hotel.objects.get(id=id_hotel)
    if request.method == "POST":
        miForm = HotelForm(request.POST)
        if miForm.is_valid():
            hotel.nombre         = miForm.cleaned_data.get("nombre")
            hotel.ciudad         = miForm.cleaned_data.get("ciudad")
            hotel.pais           = miForm.cleaned_data.get("pais")
            hotel.fecha_desde    = miForm.cleaned_data.get("fecha_desde")
            hotel.fecha_hasta    = miForm.cleaned_data.get("fecha_hasta")
            hotel.fecha_compra   = miForm.cleaned_data.get("fecha_compra")
            hotel.save()
            contexto = {"hoteles": Hotel.objects.all() }
            return render(request, "misrubros/hoteles.html", contexto)       
    else:
        miForm = HotelForm(initial={"nombre": hotel.nombre, "ciudad": hotel.ciudad, "pais": hotel.pais,
                           "fecha_desde": hotel.fecha_desde, "fecha_hasta": hotel.fecha_hasta,
                           "fecha_compra": hotel.fecha_compra}) 
    
    return render(request, "misrubros/hotelForm.html", {"form": miForm})

@login_required
def hotelDelete(request, id_hotel):
    hotel = Hotel.objects.get(id=id_hotel)
    hotel.delete()
    contexto = {"hoteles": Hotel.objects.all() }
    return render(request, "misrubros/hoteles.html", contexto)     


#___ Formularios de Traslados
@login_required
def trasladoForm(request):
    if request.method == "POST":
        miForm = TrasladoForm(request.POST)
        if miForm.is_valid():
           t_nombre          = miForm.cleaned_data.get("nombre")
           t_ciudad          = miForm.cleaned_data.get("ciudad")
           t_pais            = miForm.cleaned_data.get("pais")
           t_origen          = miForm.cleaned_data.get("origen")
           t_destino         = miForm.cleaned_data.get("destino")
           t_fecha           = miForm.cleaned_data.get("fecha")
           t_hora            = miForm.cleaned_data.get("hora")
           t_fecha_compra    = miForm.cleaned_data.get("fecha_compra")
  
           traslado = Traslado(nombre=t_nombre, ciudad=t_ciudad, pais=t_pais, origen=t_origen, 
                               destino=t_destino,
                               fecha=t_fecha, hora=t_hora, fecha_compra=t_fecha_compra)
           traslado.save()
           contexto = {"traslados": Traslado.objects.all() }
           return render(request, "misrubros/traslados.html", contexto)
    else:
        miForm = TrasladoForm()
    
    return render(request, "misrubros/trasladoForm.html", {"form": miForm})

@login_required
def trasladoUpdate(request, id_traslado):
    traslado = Traslado.objects.get(id=id_traslado)
    if request.method == "POST":
        miForm = TrasladoForm(request.POST)
        if miForm.is_valid():
            traslado.nombre          = miForm.cleaned_data.get("nombre")
            traslado.ciudad          = miForm.cleaned_data.get("ciudad")
            traslado.pais            = miForm.cleaned_data.get("pais")
            traslado.origen          = miForm.cleaned_data.get("origen")
            traslado.destino         = miForm.cleaned_data.get("destino")
            traslado.fecha           = miForm.cleaned_data.get("fecha")
            traslado.hora            = miForm.cleaned_data.get("hora")
            traslado.fecha_compra    = miForm.cleaned_data.get("fecha_compra")
            traslado.save()
            contexto = {"traslados": Traslado.objects.all() }
            return render(request, "misrubros/traslados.html", contexto)       
    else:
        miForm = TrasladoForm(initial={"nombre": traslado.nombre, "ciudad": traslado.ciudad, 
                              "pais": traslado.pais, "origen": traslado.origen,
                              "destino": traslado.destino, "fecha": traslado.fecha, "hora": traslado.hora,
                              "fecha_compra": traslado.fecha_compra}) 
    
    return render(request, "misrubros/trasladoForm.html", {"form": miForm})

@login_required
def trasladoDelete(request, id_traslado):
    traslado = Traslado.objects.get(id=id_traslado)
    traslado.delete()
    contexto = {"traslados": Traslado.objects.all() }
    return render(request, "misrubros/traslados.html", contexto) 


#___ Formularios de Alquiler de Autos
class AlquilerautoList(LoginRequiredMixin, ListView):
    model = AlquilerAuto

class AlquilerautoCreate(LoginRequiredMixin, CreateView):
    model = AlquilerAuto
    fields = ["nombre", "marca", "modelo", "ciudad", "pais", "origen", "destino", "fecha_desde", "fecha_hasta", "fecha_compra"]
    success_url = reverse_lazy("alquilerautos")

class AlquilerautoUpdate(LoginRequiredMixin, UpdateView):
    model = AlquilerAuto
    fields = ["nombre", "marca", "modelo", "ciudad", "pais", "origen", "destino", "fecha_desde", "fecha_hasta", "fecha_compra"]
    success_url = reverse_lazy("alquilerautos")

class AlquilerautoDelete(LoginRequiredMixin, DeleteView):
    model = AlquilerAuto
    success_url = reverse_lazy("alquilerautos")


#--Busqueda de Vuelos
@login_required
def buscarVuelos(request):
    return render(request, "misrubros/buscar.html")

@login_required
def encontrarVuelos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        vuelos = Vuelo.objects.filter(nombre__icontains=patron)
        contexto = {'vuelos': vuelos}    
    else:
        contexto = {'vuelos': Vuelo.objects.all()}
        
    return render(request, "misrubros/vuelos.html", contexto)

# -- Funciones de  Login, Logout y Registration


def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            #_______ Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #______________________________________________________________
            return render(request, "misrubros/index.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "misrubros/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            #usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('comenzar'))
    else:
        miForm = RegistroForm()

    return render(request, "misrubros/registro.html", {"form": miForm}) 


# -- Edición de Perfil y del Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("comenzar"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "misrubros/editarPerfil.html", {"form": miForm})
    
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "misrubros/cambiar_clave.html"
    success_url = reverse_lazy("comenzar")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #_________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #_________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________________
            return redirect(reverse_lazy("comenzar"))
    else:
        miForm = AvatarForm()
    return render(request, "misrubros/agregarAvatar.html", {"form": miForm})    