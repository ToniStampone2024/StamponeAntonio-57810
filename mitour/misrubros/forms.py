
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class VueloForm(forms.Form):
    nombre       = forms.CharField(max_length=50, required=True, label="Aerolínea")
    numero       = forms.CharField(max_length=10, required=True, label="Nro. Vuelo")
    origen       = forms.CharField(max_length=50, required=True)
    destino      = forms.CharField(max_length=50, required=True)
    fecha        = forms.DateField(required=True)
    hora         = forms.CharField(max_length=4, required=True)
    fecha_compra = forms.DateField(required=True)

class HotelForm(forms.Form):
    nombre        = forms.CharField(max_length=50, required=True)
    ciudad        = forms.CharField(max_length=50, required=True)
    pais          = forms.CharField(max_length=50, required=True)
    fecha_desde   = forms.DateField(required=True)
    fecha_hasta   = forms.DateField(required=True)
    fecha_compra  = forms.DateField(required=True)

class TrasladoForm(forms.Form):
    nombre        = forms.CharField(max_length=50, required=True, label="Empresa")
    ciudad        = forms.CharField(max_length=50, required=True)
    pais          = forms.CharField(max_length=50, required=True)
    origen        = forms.CharField(max_length=50, required=True)
    destino       = forms.CharField(max_length=50, required=True)
    fecha         = forms.DateField(required=True)
    hora          = forms.CharField(max_length=4, required=True)
    fecha_compra  = forms.DateField(required=True)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)