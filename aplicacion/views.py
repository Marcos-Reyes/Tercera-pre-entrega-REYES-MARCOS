from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import*


# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def productos(request):

    contexto = {'productos': Producto.objects.all(), 'titulo':'Listado de Productos' }
    return render(request, "aplicacion/productos.html", contexto)

def proveedor(request):
    return render(request, "aplicacion/proveedor.html")

def clientes(request):

    contexto = {'clientes': Cliente.objects.all(), 'titulo':'Listado de Clientes' }
    return render(request, "aplicacion/clientes.html", contexto)

def productoForm(request):
    if request.method == "POST":
        producto = Producto(nombre=request.POST['nombre'],
                      numero=request.POST['numero'],)
        producto.save()
        return HttpResponse("Se grabo con exito el producto")
    return render(request, "aplicacion/agregarProdructo.html")

def agregarProducto2(request):
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get('nombre')
            producto_numero = miForm.cleaned_data.get('numero')
            producto= Producto(nombre=producto_nombre,
                              numero=producto_numero,)
            producto.save()
            return HttpResponse("Se grabo con exito el producto")
        return render(request, "aplicacion/base.html")
    else:
        miForm= ProductoForm()

        return render(request, "aplicacion/agregarProducto2.html", {"form": miForm})
    
def agregarCliente(request):
    if request.method == "POST":
        miForm2 = ClienteForm(request.POST)
        if miForm2.is_valid():
            cliente_nombre = miForm2.cleaned_data.get('nombre')
            cliente_apellido = miForm2.cleaned_data.get('apellido')
            cliente_email = miForm2.cleaned_data.get('email')
            cliente= Cliente(nombre=cliente_nombre,
                              apellido=cliente_apellido,
                              email=cliente_email,)
            cliente.save()
            return HttpResponse("Se grabo con exito el Cliente")
        return render(request, "aplicacion/base.html")
    else:
        miForm2= ClienteForm()

        return render(request, "aplicacion/agregarCliente.html", {"form": miForm2})
    
def buscarCliente(request):
    return render(request, "aplicacion/buscarCliente.html")

def buscar3(request):
    if request.GET['buscar']:
        patron= request.GET['buscar']
        clientes= Cliente.objects.filter(nombre__icontains=patron)
        contexto= {"clientes": clientes, 'titulo': 'El resultado de tu busqueda',
                   'mensaje': f"No se encontraron clientes con el dato '{patron}'"}
    
        return render(request, "aplicacion/clientes.html", contexto)
   
    return HttpResponse("No se ingreso nada a buscar")
    
def buscarProducto(request):
    return render(request, "aplicacion/buscarProducto.html")
    
def buscar2(request):
    if request.GET['buscar']:
        patron= request.GET['buscar']
        productos= Producto.objects.filter(nombre__icontains=patron)
        contexto= {"productos": productos, 'titulo': 'El resultado de tu busqueda',
                   'mensaje': f"No se encontraron productos con el patron '{patron}'"}
    
        return render(request, "aplicacion/productos.html", contexto)
   
    return HttpResponse("No se ingreso nada a buscar")

def agregarProveedor(request):
    if request.method == "POST":
        miForm3 = ProveedorForm(request.POST)
        if miForm3.is_valid():
            proveedor_nombre = miForm3.cleaned_data.get('nombre')
            proveedor_apellido = miForm3.cleaned_data.get('apellido')
            proveedor_email = miForm3.cleaned_data.get('email')
            proveedor= Proveedor(nombre=proveedor_nombre,
                              apellido=proveedor_apellido,
                              email=proveedor_email,)
            proveedor.save()
            return HttpResponse("Se grabo con exito el Proveedor")
        return render(request, "aplicacion/base.html")
    else:
        miForm3= ProveedorForm()

        return render(request, "aplicacion/agregarProveedor.html", {"form": miForm3})
    
def buscarProveedor(request):
    return render(request, "aplicacion/buscarProveedor.html")

def buscar4(request):
    if request.GET['buscar']:
        patron= request.GET['buscar']
        proveedor= Proveedor.objects.filter(nombre__icontains=patron)
        contexto= {"proveedor": proveedor, 'titulo': 'El resultado de tu busqueda',
                   'mensaje': f"No se encontraron proveedores con el dato '{patron}'"}
    
        return render(request, "aplicacion/proveedor.html", contexto)
   
    return HttpResponse("No se ingreso nada a buscar")

def proveedor(request):

    contexto = {'proveedor': Proveedor.objects.all(), 'titulo':'Listado de Proveedores' }
    return render(request, "aplicacion/proveedor.html", contexto)
    
