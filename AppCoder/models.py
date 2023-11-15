from django.db import models
#Un modelo es la estructura que le creamos a un dato
# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40) #char es para str
    camada = models.IntegerField() #integer para int

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)  # char es para str
    apellido = models.CharField(max_length=30)  # char es para str
    email = models.EmailField()  # especifico para email