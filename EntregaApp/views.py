from django.shortcuts import render
from django.http import HttpResponse

from .models import Producto 

# Create your views here.






def producto(codigo, nombre, marca, precio_costo, tipo):

  nuevo_producto = Producto(codigo=codigo, nombre = nombre, marca = marca, precio_costo = precio_costo, tipo = tipo)
  nuevo_producto.save()

  return HttpResponse(f"""
    <p>Producto: {nuevo_producto.nombre} - Marca: {nuevo_producto.marca} creado!</p>
""")