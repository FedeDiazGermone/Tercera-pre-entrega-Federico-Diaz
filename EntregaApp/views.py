from django.shortcuts import render
from django.http import HttpResponse

from .models import Producto, Proveedor, Compra
from .forms import ProdFormulario, ProvFormulario, CompraFormulario
from django.shortcuts import render



TEMPLATE_INICIO = "inicio.html"

# Create your views here.

def inicio(req):
  return render(req, TEMPLATE_INICIO, {})


def producto(codigo, nombre, marca, precio_costo, tipo):

  nuevo_producto = Producto(codigo=codigo, nombre = nombre, marca = marca, precio_costo = precio_costo, tipo = tipo)
  nuevo_producto.save()

  return HttpResponse(f"""
    <p>Producto: {nuevo_producto.nombre} - Marca: {nuevo_producto.marca} creado!</p>
""")

def producto_formulario(req):
  
  if req.method == 'POST':

    formulario = ProdFormulario(req.POST)

    if formulario.is_valid():

        data = formulario.cleaned_data

        nuevo_prod = Producto(codigo=data['codigo'], nombre=data['nombre'], marca=data['marca'], precio_costo=data['precio_costo'], tipo=data['tipo'])
        nuevo_prod.save()

        return render(req, TEMPLATE_INICIO, {"message": "Producto creado con éxito"})
    
    else:

        return render(req, TEMPLATE_INICIO, {"message": "Datos no válidos"})
  
  else:

    formulario = ProdFormulario()

    return render(req, "prod_formulario.html", {"formulario": formulario})


def productos(req):
  lista = Producto.objects.all()

  return render(req, "productos.html", {"lista_productos": lista})


def lista_productos(req):

  productos = Producto.objects.all()

  return render(req, "leer_productos.html", {"productos": productos})



def proveedores(req):
  return render(req, "proveedores.html", {})

def crear_producto(req):

  if req.method == 'POST':

    formulario = ProdFormulario(req.POST)

    if formulario.is_valid():

        data = formulario.cleaned_data

        nuevo_prod = Producto(codigo=data['codigo'], nombre=data['nombre'], marca=data['marca'], precio_costo=data['precio_costo'], tipo=data['tipo'])
        nuevo_prod.save()

        return render(req, TEMPLATE_INICIO, {"message": "Producto creado con éxito"})
    
    else:

        return render(req, TEMPLATE_INICIO, {"message": "Datos no válidos"})
  
  else:

    formulario = ProdFormulario(req.POST)

    return render(req, "prod_formulario.html", {"formulario": formulario  })
  

  
def eliminar_producto(req, codigo):

  if req.method == 'POST':

    profesor = Producto.objects.get(codigo=codigo)
    profesor.delete()

    mis_productos = Producto.objects.all()

  return render(req, "leer_productos.html", {"profesores": mis_productos})


def editar_producto(req, codigo):

  if req.method == 'POST':

    formulario = ProdFormulario(req.POST)

    if formulario.is_valid():

      data = formulario.cleaned_data
      producto = Producto.objects.get(codigo=codigo)

      producto.nombre = data["nombre"]
      producto.marca = data["marca"]
      producto.precio_costo = data["precio_costo"]
      producto.tipo = data["tipo"]

      producto.save()

      return render(req, TEMPLATE_INICIO, {"message": "Producto actualizado con éxito"})
    
    else:

      return render(req, TEMPLATE_INICIO, {"message": "Datos no válidos"})
  
  else:

    producto = Producto.objects.get(codigo=codigo)

    formulario = ProdFormulario(initial={
      "nombre": producto.nombre,
      "marca": producto.marca,
      "precio_costo": producto.precio_costo,
      "tipo": producto.tipo,
    })

    return render(req, "editar_producto.html", {"formulario": formulario, "codigo": producto.codigo})
  

def busqueda_marca(req):

    return render(req, "busqueda_marca.html", {})


def buscar(req):

  marca = req.GET.get("marca")  
  if marca:
    ### marca = req.GET["marca"]

    productos = Producto.objects.filter(marca__icontains=marca)

    return render(req, "resultadoBusqueda.html", {"productos": productos, "marca": marca})
  else:      
      return render(req, TEMPLATE_INICIO, {"message": "No envias el dato de la marca"})


#### Proveedor

def proveedor(codigo, nombre, email, telefono):

  nuevo_prov = Proveedor(nombre=nombre, codigo=codigo, email=email, telefono=telefono)
  nuevo_prov.save()

  return HttpResponse(f"""
    <p>Código: {nuevo_prov.codigo} - Nombre: {nuevo_prov.nombre} creado!</p>
  """)


def proveedor_formulario(req):

  print('method: ', req.method)
  print('POST: ', req.POST)

  if req.method == 'POST':

    formulario = ProvFormulario(req.POST)

    if formulario.is_valid():

      data = formulario.cleaned_data

      nuevo_prov = Proveedor(codigo=data['codigo'], nombre=data['nombre'], email=data['email'], telefono=data['telefono'])
      nuevo_prov.save()

      return render(req, TEMPLATE_INICIO, {"message": "Proveedor creado con éxito"})
    
    else:

      return render(req, TEMPLATE_INICIO, {"message": "Datos inválidos"})
  
  else:

    formulario = ProvFormulario()

    return render(req, "prov_formulario.html", {"formulario": formulario})


## Compras

def compra(nro, fecha_compra, entregado, cantidad, precio_venta):

  nueva_comp = Compra(nro=nro, fecha_compra=fecha_compra, entregado=entregado, cantidad=cantidad, precio_venta=precio_venta)
  nueva_comp.save()

  return HttpResponse(f"""
    <p>Código: {nueva_comp.nro} - Nombre: {nueva_comp.fecha_compra} creada!</p>
  """)


def compra_formulario(req):

  print('method: ', req.method)
  print('POST: ', req.POST)

  if req.method == 'POST':

    formulario = CompraFormulario(req.POST)

    if formulario.is_valid():

      data = formulario.cleaned_data
      
      nueva_comp = Compra(
                nro=data['nro'],
                fecha_compra=data['fecha_compra'],
                entregado=data['entregado'],
                cantidad=data['cantidad'],
                precio_venta=data['precio_venta'],                
            )
      nueva_comp.save()

      return render(req, TEMPLATE_INICIO, {"message": "Compra creada con éxito"})
    
    else:

      return render(req, TEMPLATE_INICIO, {"message": "Datos inválidos"})
  
  else:

    formulario = CompraFormulario()

    return render(req, "compra_formulario.html", {"formulario": formulario})