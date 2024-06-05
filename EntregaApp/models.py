from django.db import models

# Create your models here.

class Producto(models.Model):

  codigo = models.CharField(max_length=30)
  nombre = models.CharField(max_length=30)
  marca = models.CharField(max_length=30)  
  precio_costo = models.FloatField()  
  tipo = models.CharField(max_length=30)

  def __str__(self):    
    return f'{self.nombre} - {self.marca} - {self.precioCosto} - {self.precioVenta} - {self.tipo }'
  
class Proveedor(models.Model):

  codigo = models.CharField(max_length=30)
  nombre = models.CharField(max_length=30)  
  email = models.EmailField()
  telefono = models.CharField(max_length=30)
  marca = models.CharField(max_length=30)   

  def __str__(self):    
    return f'{self.codigo} - {self.nombre} - {self.marca} - {self.email} - {self.telefono}'

class Compra(models.Model):

  nro = models.IntegerField()
  fecha_compra = models.DateField()
  entregado = models.BooleanField()
  cantidad = models.IntegerField()  
  precio_venta = models.FloatField()
  ## producto = models.ForeignKey(Producto, on_delete=models.CASCADE)    
  ## proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)    

  def __str__(self):    
    return f'{self.nro} - {self.fecha_compra} - {self.entregado} - {self.cantidad}'

