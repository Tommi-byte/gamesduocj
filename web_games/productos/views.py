from django.shortcuts import render, get_object_or_404
from .models import Producto
# Create your views here.

def verProductos(request):
    productos = Producto.objects.all()
    return render(request,  "productos.html", {"productos":productos})

def detalleProducto(request, prod_id):
    #Buscar el producto que tiene ese id
    #producto = Producto.objects.get(id = prod_id)
    producto = get_object_or_404(Producto, id=prod_id)
    return render(request, "ver_producto.html", {'producto':producto})
