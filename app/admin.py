from django.contrib import admin
from .models import Cliente, Estado, Producto, Repartidor, Pedido

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Estado)
admin.site.register(Producto)
admin.site.register(Repartidor)
admin.site.register(Pedido)