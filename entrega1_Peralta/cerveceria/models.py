from datetime import datetime
from django.db import models
from django import forms

# Create your models here.


## tipos de producto a la venta

class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    tipo_producto = models.CharField(max_length=40)
    fecha_registro = models.DateField()
    
## estilos de cerveza

class Estilos(models.Model):
    nombre = models.CharField(max_length=40)
    ibu = models.IntegerField()
    alcohol = models.IntegerField()
    cuerpo = models.CharField(max_length=20)
    amargor = models.CharField(max_length=20)
    aroma = models.CharField(max_length=20)
    temp_cons = models.IntegerField()


## Personal de la cerveceria

class Staffs(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cargo = models.CharField(max_length=40)
    fecha_ingreso = models.DateField()


