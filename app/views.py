from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cliente, Estado, Producto, Repartidor, Pedido
from django.contrib import messages

# Create your views here.


def home(request):
    pedidos = Pedido.objects.all()
    estados = Estado.objects.all()
    data = {
        'pedidos': pedidos,
        'estados': estados
    }
    return render(request, 'app/home.html', data)

def detalle(request):
    return render(request, 'app/detalle.html')

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    estados = Estado.objects.all()
    context = {
        'pedidos': pedidos,
        'estados': estados
    }
    return render(request, 'tu_app/lista_pedidos.html', context)

def actualizar_estado_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    if request.method == 'POST':
        nuevo_estado_id = request.POST.get('nuevo_estado')
        nuevo_estado = get_object_or_404(Estado, id=nuevo_estado_id)
        
        pedido.estado_pedido = nuevo_estado
        pedido.save()
        messages.success(request,"Modificado Correctamente, Se ha enviado un correo al Cliente con el nuevo estado de su pedido")
        return redirect('home')
    
def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    pedidos = Pedido.objects.filter(nombre_pedido=cliente)
    context = {
        'cliente': cliente,
        'pedidos': pedidos
    }
    return render(request, 'app/detalle.html', context)