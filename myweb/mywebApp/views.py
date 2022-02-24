from distutils.command.sdist import sdist
from venv import create
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.views import LogoutView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from productos.models import Producto
from .forms import UserRegisterForm,UserEditForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request,'mywebApp/home.html')


def login_request(request):
    if request.method=='POST':
        form= AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            
            user = authenticate(username=usuario,password=contra)

            if user is not None:
                login(request,user)
                
                return render(request,'mywebApp/home.html', {'mensaje':f'Bienvenido {usuario}'})
            else:
                return render(request,'mywebApp/login.html',
                #return render(request,'mywebApp/home.html', {'mensaje':'Error, datos incorrectos'})
                    {'form':form,
                    'error':'No es valido el usuario y contraseña'})

        else:
            #return render(request,'mywebApp/home.html', {'mensaje':'Error, formulario erroneo'})
            return render(request,'mywebApp/login.html',{'form':form})
    else:
        form=AuthenticationForm()
        return render(request,'mywebApp/login.html',{'form':form})

    #return render(request,'mywebApp/login.html',{'form':form})


class ProductoListView(ListView):
    model=Producto
    template_name='mywebApp/producto_lista.html'
    context_object_name='productos'

class ProductoDetalle(DetailView):
    model = Producto
    template_name = 'mywebApp/producto_detalle.html'

class ProductoNuevo(CreateView):
    model = Producto
    success_url = reverse_lazy('productos')
    fields = ['nombre','servicio','precio']
    template_name = 'mywebApp/producto_nuevo.html'

class ProductoUpdate(UpdateView):
    model = Producto
    success_url = reverse_lazy('productos')
    fields = ['nombre','servicio','precio']
    template_name = 'mywebApp/producto_nuevo.html'

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')
    template_name='mywebApp/producto_confirm_delete.html'

  


def register(request):
    if request.method == 'POST':
        formu = UserRegisterForm(request.POST)

        if formu.is_valid():
            username = formu.cleaned_data['username']
            formu.save()
            return HttpResponse(f'Usuario {username} creado correctamente')
    else:
        formu = UserRegisterForm()
    return render(request,'mywebApp/registro.html',{'formu': formu})


class UserCreate(CreateView):
    model = User
    success_url = reverse_lazy('Login')
    template_name='mywebApp/registro.html'
    form_class=UserRegisterForm

# class UsuarioUpdate(UpdateView):
#     model = User
#     success_url = reverse_lazy('login')
#     fields = ['email','password1','password2']
#     template_name = 'mywebApp/editar_usuario.html'

@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data['email']
            usuario.password1 = data['password1']
            usuario.password2 = data['password2']
            usuario.save()
            return render(request,'mywebApp/home.html')

    else:
        formulario = UserEditForm({'email': usuario.email})

    return render(request,'mywebApp/editar_usuario.html',{'miform':formulario, 'usuario':usuario})