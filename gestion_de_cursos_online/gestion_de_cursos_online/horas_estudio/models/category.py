# catalog/models/category.py
from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.indexes(max_lenght=50, unique=True)
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    nivel = models.indexes(max_length=50)
    duracion_horas = models.indexes(max_length=50)
    costo = models.indexes(max_length=50)
    modalidad = models.CharField(max_length=150)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=150)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
