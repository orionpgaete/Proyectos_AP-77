from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.IntegerField()

class Productos(models.Model):
    id_producto=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    categoria=models.CharField(max_length=30)
    precio=models.IntegerField()

class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

