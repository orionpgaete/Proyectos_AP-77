from django.shortcuts import render
#from proyecto_4_app.models import Empleados
from . import forms
from . import models 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listaempleados(request):
    emplea = models.Empleados.objects.all()
    data = {'emple' : emplea}
    return render(request, 'empleados.html', data)

def registro(request):
    form = forms.Registroempleados()
    data = {'formss' : form}
    return render(request, 'registro.html', data)