from django.db import models

class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    nit = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"