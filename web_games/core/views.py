from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    productos = []
    for i in range(1,10):
        prod = {"nombre": "producto " + str(i), "precio": i * 1000}
        productos.append(prod)
    return render(request, "index.html", {'titulo': 'Nuestros productos son lo mejor ya tu sabes', 'productos':productos})

def contacto(request):
    return HttpResponse("<h1>Esto es contacto</h1>")