from django.contrib import admin
from .models import Entidad, Cliente, Recibo, Pago

admin.site.register(Entidad)
admin.site.register(Cliente)
admin.site.register(Recibo)
admin.site.register(Pago)
