from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.views import LogoutView
from django.views.generic import ListView

from productos.models import Producto

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