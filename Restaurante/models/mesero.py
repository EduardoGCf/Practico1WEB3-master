from django.db import models

class Mesero(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"