from django.db import models
from django.contrib.auth.models import User


CATEGORIAS_GASTO = [
    ('Comida', 'Comida'),
    ('Transporte', 'Transporte'),
    ('Entretenimiento', 'Entretenimiento'),
    ('Educación', 'Educación'),
    ('Otros', 'Otros'),
]

CATEGORIAS_INGRESO = [
    ('Salario', 'Salario'),
    ('Venta', 'Venta'),
    ('Regalo', 'Regalo'),
    ('Otros', 'Otros'),
]


class Gasto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_GASTO)
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.monto} ({self.usuario.username})"


class Ingreso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_INGRESO)
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.monto} ({self.usuario.username})"
