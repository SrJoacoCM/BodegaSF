from django.urls import path
from .views import home,detalle, lista_repartidores, pedidos_repartidor
from app import views
urlpatterns = [
    path('', home, name="home"),
    path('detalle/', detalle, name="detalle"),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pedido_id>/actualizar_estado/', views.actualizar_estado_pedido, name='actualizar_estado_pedido'),
    path('detalle_cliente/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('repartidores/', lista_repartidores, name='lista_repartidores'),
     path('repartidores/<int:repartidor_id>/pedidos/', pedidos_repartidor, name='pedidos_repartidor'),
]
