from django.contrib import admin
from cad.cliente.models import Customer, CustomerAddress
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerAddress)
