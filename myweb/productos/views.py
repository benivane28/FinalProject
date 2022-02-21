from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto
#from .models import ProductoList
# Create your views here.
def productos(request):
    productos = Producto.objects.all()
    return render(request,'productos/productos.html', {'productos':productos})

def busqueda_producto(request):
    return render(request, 'productos/busqueda_producto.html')

def buscar(request):

    if request.GET['prd']:

        producto=request.GET['prd']
        productos=Producto.objects.filter(nombre__icontains=producto)
        return render(request,'productos/resultado_busqueda.html', {'productos':productos, 'query':producto})
    else:
        mensaje='No haz introducido nada'
    return HttpResponse(mensaje)


#def ProductoList(request):
    #return render(request,'productos/producto_lista.html')