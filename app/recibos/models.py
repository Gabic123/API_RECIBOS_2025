from django.db import models

class Entidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Recibo(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.entidad} - {self.valor}"

class Pago(models.Model):
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    valor_pagado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago de {self.valor_pagado} el {self.fecha_pago}"
