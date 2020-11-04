from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.verProductos, name="productos"),
    path('producto/<int:prod_id>', views.detalleProducto, name="producto")
]