from django.shortcuts import render, redirect
from .models import Proyecto
from . import forms
# Create your views here.

def index(request):
    return render(request, 'index.html')


def listarproyecto(request):
    pro = Proyecto.objects.all()
    data = {'proyec': pro}

    return render(request, 'proyecto.html', data)


def agregarProyecto(request):
    form = forms.FormProyecto()
    if (request.method == 'POST'):
        form = forms.FormProyecto(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)

    data = {'form': form}
    return render(request, 'agregar.html', data)

def eliminarProyecto(request, id):
    pro = Proyecto.objects.get(id = id)
    pro.delete()
    return redirect('/proyectos')


def modificarProyecto(request, id):
    pro = Proyecto.objects.get(id = id)
    form = forms.FormProyecto(instance=pro)
    if (request.method == 'POST'):
        form = forms.FormProyecto(request.POST, instance=pro)
        if (form.is_valid()):
            form.save()
        return index(request)

    data = {'form': form}
    return render(request, 'agregar.html', data)