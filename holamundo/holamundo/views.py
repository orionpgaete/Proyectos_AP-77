from django.http import HttpResponse

#aca creamos vistas

def hola(request):
    return HttpResponse("<h1>Hola alumnos bienvenido a Django</h1>")


def chaoo(request):
    return HttpResponse("nos vemos")
