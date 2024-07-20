from django.db import models
from django.contrib.auth.models import User

# Modelo del Negocio de la Aplicacion misrubros

class Vuelo(models.Model):
    nombre       = models.CharField(max_length=50)
    numero       = models.CharField(max_length=10)
    origen       = models.CharField(max_length=50)
    destino      = models.CharField(max_length=50)
    fecha        = models.DateField()
    hora         = models.CharField(max_length=4)
    fecha_compra = models.DateField()

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}"

class Hotel(models.Model):
    nombre        = models.CharField(max_length=50)
    ciudad        = models.CharField(max_length=50)
    pais          = models.CharField(max_length=50)
    fecha_desde   = models.DateField()
    fecha_hasta   = models.DateField()
    fecha_compra  =models.DateField()

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}"

class Traslado(models.Model):
    nombre        = models.CharField(max_length=50)
    ciudad        = models.CharField(max_length=50)
    pais          = models.CharField(max_length=50)
    origen        = models.CharField(max_length=50)
    destino       = models.CharField(max_length=50)
    fecha         = models.DateField()
    hora          = models.CharField(max_length=4)
    fecha_compra  = models.DateField()

    class Meta:
        verbose_name = "Traslado"
        verbose_name_plural = "Traslados"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}"

class AlquilerAuto(models.Model):
    nombre        = models.CharField(max_length=50)
    marca         = models.CharField(max_length=50)
    modelo        = models.CharField(max_length=50)
    ciudad        = models.CharField(max_length=50)
    pais          = models.CharField(max_length=50)
    origen        = models.CharField(max_length=50)
    destino       = models.CharField(max_length=50)
    fecha_desde   = models.DateField()
    fecha_hasta   = models.DateField()
    fecha_compra  = models.DateField()

    class Meta:
        verbose_name = "AlquilerAuto"
        verbose_name_plural = "AlquilerAutos"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}, {self.marca}, {self.modelo}, {self.ciudad}, {self.pais}"


class Avatar(models.Model):   
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"    