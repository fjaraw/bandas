from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cantante = models.BooleanField(default=False)
    instrumento = models.CharField(max_length=50)

class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    artistas = models.ManyToManyField(Artista, through="ArtistaGrupo", related_name="grupos")

class ArtistaGrupo(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    creacion_registro = models.DateField(auto_now_add=True)
    agregado_por = models.CharField(max_length=50)

class Album(models.Model):
    titulo = models.CharField(max_length=50)
    year = models.IntegerField()
    grupo = models.ForeignKey(Grupo,related_name="albumes",on_delete=models.CASCADE)