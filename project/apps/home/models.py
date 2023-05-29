from django.db import models

# Create your models here.

class Usuario(models.Model):
    """
    Usuario de la aplicación. Puede ser una persona potencial para transitar animales o representantes de la organizaciones protectoras de animales aptos para cargar animales para transitar.
    """
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.apellido
    

class Animales(models.Model):
    """
    Tipo de animal disponible para transitar.
    """
    Animal = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.Animal


class Region(models.Model):
    """
    Área de la cobertura de la organización protectora de animales.
    """
    nombre = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.nombre
    

class Organizacion(models.Model):
    """
    Organizaciones protectoras de animales que poseen la responsabilidad del animal en tránsito encargadas de gestionar la adopción.
    """
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    region_id = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Zona de cobertura: {self.region_id} "

class Sexo(models.Model):
    """
    Sexo de los animales disponibles para transitar.
    """
    sexo = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.sexo
    
class Transito(models.Model):
    """
    Animal disponible para transitar hasta su adopción definitiva.
    """
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    organizacion_id = models.ForeignKey(Organizacion, on_delete=models.SET_NULL, null=True)
    sexo_id = models.ForeignKey(Sexo, on_delete=models.SET_NULL, null=True)
    animal_id = models.ForeignKey(Animales, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Animal: {self.animal_id}, Edad: {self.edad}, Organización: {self.organizacion_id}"