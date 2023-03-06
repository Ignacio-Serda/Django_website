from django.db import models

class Curso(models.Model):
    nombre=models.CharField(max_length=200)
    codigo=models.IntegerField()

class Estudiante(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    email=models.EmailField()
    
class Pruebas(models.Model):
    tema=models.CharField(max_length=200)
    nota=models.IntegerField()
    aprobado=models.BooleanField()