from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=100, blank=False)
    descripcion = models.TextField(blank=False)
    completado = models.BooleanField(default=False)
    fecha = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo