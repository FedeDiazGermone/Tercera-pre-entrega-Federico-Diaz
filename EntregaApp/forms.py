from django import forms
from .models import Producto, Proveedor

class ProdFormulario(forms.Form):

  codigo = forms.CharField(max_length=30)
  nombre = forms.CharField(max_length=30)
  marca = forms.CharField(max_length=30)  
  precio_costo = forms.FloatField()  
  tipo = forms.CharField(max_length=30)


class ProvFormulario(forms.Form):

  codigo = forms.CharField(max_length=30)
  nombre = forms.CharField(max_length=30)  
  email = forms.EmailField()
  telefono = forms.CharField(max_length=30)  


class CompraFormulario(forms.Form):

  nro = forms.IntegerField()
  fecha_compra = forms.DateField()
  entregado = forms.BooleanField()
  cantidad = forms.IntegerField()  
  precio_venta = forms.FloatField()
  ##producto = forms.ModelChoiceField(queryset=Producto.objects.all())
  ##  proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all())