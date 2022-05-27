from django.db import models
from cad.cliente.models import *


class contrato(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, verbose_name="Cliente")
    num = models.CharField(max_length=100000, null=True, blank=True, verbose_name="Numero de Contrato")
    description = models.CharField(max_length=250, null=True, verbose_name="descripción")
    date_inicio = models.DateField(null=True, verbose_name="Fecha de Inicio")
    date_final = models.DateField(null=True, verbose_name="Fecha Fin")
    cont = models.FileField(upload_to='contrato/%Y/%m/%d', null=True, blank=True, verbose_name="Archivo")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.num

    class Meta:
        db_table = 'contrato'
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ['num']
