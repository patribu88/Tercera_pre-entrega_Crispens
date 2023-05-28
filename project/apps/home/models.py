from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.apellido
    

class Animales(models.Model):
    Animal = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.Animal