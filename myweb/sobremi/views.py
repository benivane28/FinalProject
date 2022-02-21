from django.shortcuts import render
#from sobremi.models import Creadora

# Create your views here.
def sobremi(request):
    #creadoras=Creadora.objects.all()
    return render(request,'sobremi/sobremi.html')

def vermas(request):
    return render(request,'sobremi/vermas.html')