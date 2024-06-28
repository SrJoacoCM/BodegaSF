from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.IntegerField()
    direccion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Estado(models.Model):
    estado = models.CharField(max_length=200)
    
    def __str__(self):
        return self.estado

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Repartidor(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    nombre_pedido = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='pedidos_nombre')
    estado_pedido = models.ForeignKey(Estado, on_delete=models.PROTECT)
    repartidor_pedido = models.ForeignKey(Repartidor, on_delete=models.PROTECT)
    producto_pedido = models.ForeignKey(Producto, on_delete=models.PROTECT,  null=True, blank=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre_pedido.nombre}'