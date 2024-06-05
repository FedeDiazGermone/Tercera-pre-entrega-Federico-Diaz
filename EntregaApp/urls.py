from django.urls import path
from EntregaApp.views import inicio, productos, crear_producto,editar_producto,eliminar_producto, lista_productos, producto_formulario, buscar,proveedor_formulario,compra_formulario, busqueda_marca

urlpatterns = [
    path("", inicio, name='inicio'),
    path('productos/', productos, name='productos'),
        
    path('producto-formulario/', producto_formulario, name='producto_formulario'), 
    path('lista-productos/', lista_productos, name='ListaProductos'),
    
    path('crea-producto/', crear_producto, name='CreaProducto'),
    path('elimina-producto/<int:codigo>', eliminar_producto, name='EliminaProducto'),
    path('edita-producto/<int:codigo>', editar_producto, name='EditaProducto'),
    path('busqueda-marca/', busqueda_marca, name='BusquedaMarca'),
    path('buscar/', buscar, name='BuscarMarca'),  
    path('proveedor-formulario/', proveedor_formulario, name='proveedor_formulario'), 
    path('compra-formulario/', compra_formulario, name='compra_formulario'), 
]
