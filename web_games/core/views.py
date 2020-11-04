from django.shortcuts import render, HttpResponse
from productos.models import Producto

# Create your views here.
def home(request):
    #En el slider aparezcan solo los productos que estan en oferta
    productos = Producto.objects.filter(estaEnOferta=True)

    return render(request, "index.html", {'titulo': 'Nuestros productos son lo mejor ya tu sabes',
    'productos':productos })

def contacto(request):
    
    return render(request,"contacto.html")