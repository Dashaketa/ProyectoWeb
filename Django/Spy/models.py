from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=9)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"