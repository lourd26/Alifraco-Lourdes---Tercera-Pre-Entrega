from django.http import HttpResponse
from django.template import Template,Context,loader
from django.shortcuts import render
from comienzo.models import Acolchados

def comienzo(request):
    # return HttpResponse("Bienvenidos")
    return render(request,"comienzo/index.html")

def template1(request):
     return render(request,"template1.html")

def acerca_de_mi(request):
    return render(request,"comienzo/acerca_de_mi.html")

def crear_acolchados(request,tamanio,color,composicion):
    acolchados=Acolchados(tamanio=tamanio,color=color,composicion=composicion)
    acolchados.save()
    return render(request,"comienzo/creacion_acolchado.html",{"acolchados":acolchados})