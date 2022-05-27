from django.db import models
from datetime import datetime
import json
from django.db.models import Max
from cad.user.models import *


class Customer(models.Model):
    code = models.CharField(max_length=14, null=True)
    name = models.CharField(max_length=300, null=True, verbose_name="Razón social")
    short_name = models.CharField(max_length=10, null=True, verbose_name="Nombre corto")
    ruc = models.CharField(max_length=14, null=True, verbose_name="Número ruc")
    contact = models.CharField(max_length=300, null=True, verbose_name="Nombre de contacto")
    phone = models.CharField(max_length=8, null=True, verbose_name="Teléfono")
    invoice_ext = models.CharField(max_length=8, null=True, blank=True, verbose_name="Extensión")
    invoice_movil1 = models.CharField(max_length=8, null=True, blank=True, verbose_name="Móvil 1")
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True, verbose_name="Logo")
    active = models.BooleanField(default=True)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.name, self.ruc)

    def get_image(self):
        if self.avatar:
            return f'{settings.MEDIA_URL}{self.avatar}'
        return f'{settings.STATIC_URL}img/empty.png'

    @staticmethod
    def get_code():
        code = 1
        sets = Customer.objects.filter(code__isnull=False)
        if sets:
            maxi = str(sets.aggregate(Max('code'))['code__max'])
            code = int(maxi) + 1
        return str(code).zfill(7)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.get_code()
        super().save(*args, **kwargs)

    def users(self):
        return User.objects.filter(customer=self)

    def addresses(self):
        return CustomerAddress.objects.filter(customer=self)

    def to_json(self):
        o = super().to_json()
        o['addresses'] = [d.to_json() for d in CustomerAddress.objects.filter(customer=self)]
        o['image'] = self.get_image()
        return o

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']


class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name='addresses')
    address = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'direccion'
        verbose_name = "direccion"
        verbose_name_plural = "direcciones"
