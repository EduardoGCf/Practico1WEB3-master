from django.db import models

from .cliente import Cliente
from .mesero import Mesero
from .mesa import Mesa
from .platos import Plato

class Orden(models.Model):
    ESTADO_CHOICES = [
        ('En Proceso', 'En Proceso'),
        ('Cerrado', 'Cerrado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    mesero = models.ForeignKey(Mesero, on_delete=models.CASCADE, null=True, blank=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True, blank=True)
    platos = models.ManyToManyField(Plato)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='En Proceso')
    fecha = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"Orden {self.id}"