from django.urls import path, include
from .views import*
urlpatterns = [
    path('', home, name="home"),
    path('producto/', productos, name="productos"),
    path('proveedor/', proveedor, name="proveedor"),
    path('clientes/', clientes, name="clientes"),
    path('producto_form/', productoForm, name="producto_form"),
    path('agregar_producto/', agregarProducto2, name="agregar_producto"),
    path('agregar_cliente/', agregarCliente, name="agregar_cliente"),
    path('buscar_cliente/', buscarCliente, name="buscar_cliente"),
    path('buscar_producto/', buscarProducto, name="buscar_producto"),
    path('buscar3/', buscar3, name="buscar3"),
    path('buscar2/', buscar2, name="buscar2"),
    path('agregar_proveedor/', agregarProveedor, name="agregar_proveedor"),
    path('buscar_proveedor/', buscarProveedor, name="buscar_proveedor"),
    path('buscar4/', buscar4, name="buscar4"),

]
