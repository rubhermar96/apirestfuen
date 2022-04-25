from django.db import models

# Create your models here.

class Puntodeinteres(models.Model):
    titulo = models.CharField(max_length=100,blank=False,default='')
    imagen_destacada = models.CharField(max_length=100,blank=False,default='')
    horario = models.TextField(blank=False,default='')
    descripcion = models.TextField(blank=False, default='')
    imagenes = models.TextField(blank=False, default='')
    videos = models.TextField(blank=True,default='')

    def __str__(self):
        return f"ID: ({self.pk}) | {self.titulo}"

class Beacons(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    puntodeinteres = models.CharField(max_length=100,blank=True,null=True)
    texto = models.TextField(blank=True, default='')
    conexiones = models.IntegerField(max_length=20, blank=True, default=0)

    def __str__(self):
        return f"ID: ({self.pk}) | {self.nombre} | {self.puntodeinteres}"
