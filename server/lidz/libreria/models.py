from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    CATEGORIAS = (
        ("Fantasia", "Fantasia"),
        ("Matematicas", "Matematicas"),
        ("Fisica", "Fisica")
    )
    
    titulo = models.CharField(max_length=512)
    categoria = models.CharField(max_length=255, choices=CATEGORIAS)
    autor = models.ManyToManyField(Autor, related_name="autor")
    unidades = models.IntegerField(default=0)
    

    def __str__(self):
        return self.titulo
    
# class Prestamo(models.Model):
#     libro = models.ForeignKey(Libro)
#     cliente = models.ForeignKey(User, on_delete=models.CASCADE)