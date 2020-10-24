from django.shortcuts import render
from .models import Producto
# Create your views here.

def verProductos(request):
    productos = Producto.objects.all()
    return render(request,  "productos.html", {"productos":productos})
