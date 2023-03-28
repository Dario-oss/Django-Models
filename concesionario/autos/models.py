from django.db import models

# Create your models here.
class autos(models.Model):
    marca=models.CharField(max_length=20)
    nombre=models.CharField(max_length=30)
    modelo=models.IntegerField()
    color=models.CharField(max_length=20)

class clientes(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    direccion=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    telefono=models.CharField(max_length=20)