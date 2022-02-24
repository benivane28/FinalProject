"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from productos import views
from mywebApp.views import login_request,LogoutView,ProductoListView,register,ProductoDetalle,ProductoNuevo,ProductoUpdate,ProductoDelete,editar_perfil,UserCreate
from sobremi.views import vermas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mywebApp.urls')),
    path('servicios/',include('servicios.urls')),
    path('sobremi/',include('sobremi.urls')),
    path('contacto/', include('contacto.urls')),
    path('productos/', include('productos.urls')),
    path('busqueda_producto/', views.busqueda_producto,name='BusquedaProducto'),
    path('buscar/', views.buscar),
    path('login',login_request,name='Login'),
    path('logout',LogoutView.as_view(template_name='mywebApp/logout.html'),name='Logout'),
    path('list/',ProductoListView.as_view(template_name='mywebApp/producto_lista.html'),name='productos'),
    path('vermas/',vermas,name='vermas'),
    path('register',register,name='Registro'),
    path('edit/', editar_perfil,name='user_editar'),
    path('detalle/<pk>',ProductoDetalle.as_view(),name='Detalle'),
    path('nuevo/',ProductoNuevo.as_view(),name='Crear'),
    path('update/<pk>',ProductoUpdate.as_view(),name='Actualizar'),
    path('delete/<pk>',ProductoDelete.as_view(),name='Borrar'),
]
