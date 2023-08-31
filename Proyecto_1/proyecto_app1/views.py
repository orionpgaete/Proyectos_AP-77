from django.shortcuts import render

# Create your views here.

def usotemplate(request):
    data = {"nombre" : "Pedro"}
    return render(request, 'templateapp1/plantilla.html', data)

def infoUsuario(request):
    data = {"id": "123", "nombre": "Pedro Gaete", "email": "pedro@gmail.com"}
    return render(request, 'templateapp1/userInfoTemplate.html', data)

