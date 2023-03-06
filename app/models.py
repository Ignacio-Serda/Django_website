from django.db import models

class Curso(models.Model):
    nombre=models.CharField(max_length=200)
    codigo=models.IntegerField()

class Estudiante(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    email=models.EmailField()