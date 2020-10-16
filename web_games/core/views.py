from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hola mundo desde Home</h1>")

def contacto(request):
    return HttpResponse("<h1>Esto es contacto</h1>")