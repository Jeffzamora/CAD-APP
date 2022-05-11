from django.db import models
from cad.cliente.models import *


class ingreso(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, verbose_name="Cliente")
    num = models.BigIntegerField(null=True, blank=True, verbose_name="Numero de ingreso")
    description = models.CharField(max_length=250, null=True, verbose_name="Descripción")
    date_inicio = models.DateField(null=True, verbose_name="Fecha de Entrada")
    cont = models.FileField(upload_to='ingre/%Y/%m/%d', null=True, blank=True, verbose_name="Archivo")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.num

    class Meta:
        db_table = 'ingreso'
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
        ordering = ['num']
