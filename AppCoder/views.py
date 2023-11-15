from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.
def crear_curso(request):
    curso = Curso(nombre="Python", camada=47785)
    curso.save()
    return HttpResponse(f"Su curso de {curso.nombre} y su ID es {curso.camada}")
