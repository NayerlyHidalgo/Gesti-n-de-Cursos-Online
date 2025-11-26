# catalog/models/category.py
from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.indexes(max_length=50, unique=True)
    titulo = models.CharField(max_length=150, unique=True)
    subtitulo = models.CharField(max_length=150, unique=True)
    descripcion = models.CharField(max_length=200)
    nivel = models.indexes(max_length=50)
    duracion_horas = models.DateTimeField(auto_now_add=True)
    costo = models.indexes(max_length=50)
    modalidad = models.Charfield(max_length=150)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=150)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.id
