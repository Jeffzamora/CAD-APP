from django.db import models
from cad.cliente.models import *
from cad.choices import *


class solicitudes(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, verbose_name="Cliente")
    num = models.BigIntegerField(null=True, blank=True, verbose_name="Numero de solicitude")
    description = models.CharField(max_length=250, null=True, verbose_name="Descripción")
    nivel = models.CharField(max_length=250, null=True, verbose_name="Tipo de solicitud: CAJA,FOLDER Y DOCUMENTO")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    type = models.IntegerField(choices=TIPO_CHOICES, default=1, verbose_name="Tipo de Envio")
    date_inicio = models.DateTimeField(null=True, blank=True, verbose_name='Fecha y ahora atendida')
    cont = models.FileField(upload_to='solici/%Y/%m/%d', null=True, blank=True, verbose_name="Archivo")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.num

    class Meta:
        db_table = 'solicitud'
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering = ['num']
