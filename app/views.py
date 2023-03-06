from django.shortcuts import render
from django.http import HttpResponse
from app.models import Curso

def inicio(request):
    return HttpResponse("Hola")

def template(request, name, code):
    curso = Curso(nombre=name, codigo=code)
    curso.save()
    return HttpResponse("Se ha guardado los datos")


def variables(request):
    contexto={
        "nombre":"Nacho",
        "apellido":"Serdá",
        "lista":[1,23,4],
    }
    return render(request, "template1.html", context=contexto)

def fachero(request):
    return render(request, "index.html")