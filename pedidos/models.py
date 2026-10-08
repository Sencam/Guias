from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length= 50 )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length = 100)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre