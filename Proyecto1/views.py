from django.http import HttpResponse
import datetime
from django.template import Context, Template, loader 


def saludar(request):
    return HttpResponse("hola mundo!")


def  dia_de_hoy(request):
    dia=datetime.datetime.today()
    cadena="Hoy es: "+str(dia)
    return HttpResponse(cadena)

def saludo_con_nombre(self, nombre):

    return HttpResponse("<h1>Hola mi nombre es: "+nombre+"</h1>")

def calcula_año_nacimiento(self, edad):
    return HttpResponse ("<h1>Tu año de nacimiento es: "+str(int(datetime.datetime.now().year)-int(edad))+"</h1>")



def probandoHtmL(self):

        nom="Guido"
        ape="Choque"
        lista_de_notas=[9,5,8,7,6,3,2]


        diccionario={'nombre':nom,'apellido':ape, 'lista':lista_de_notas}

        plantilla=loader.get_template('template1.html')

        documento=plantilla.render(diccionario)

        return HttpResponse(documento)