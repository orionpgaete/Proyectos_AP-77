import datetime
from django.http import HttpResponse

#aca creamos vistas

def hola(request):
    return HttpResponse("<h1>Hola alumnos bienvenido a Django</h1>")


def chaoo(request):
    return HttpResponse("nos vemos")

def chaoo2(request):
    docu = """
            <html>
                <body>
                    <h1>Hola de nuevo </h1>
                <body>
            </html>"""
    return HttpResponse(docu)

def horaactual(request):
    fecha_actual = datetime.datetime.now()
    docu = """
            <html>
                <body>
                    <h1>La Fecha y Hora actual es: %s</h1>
                <body>
            </html>""" % fecha_actual
    return HttpResponse(docu)


def calculo(request, anio, edad):
    #edad = 18
    periodo = anio - 2023
    edadfutura = edad + periodo
    docu = """
            <html>
                <body>
                    <h1>En el año %s tendras %s años</h1>
                <body>
            </html>""" % (anio, edadfutura)
    return HttpResponse(docu)




