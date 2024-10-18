from django.http import HttpResponse
from django.template import Template,Context,loader
from django.shortcuts import render,redirect
from comienzo.models import Acolchados
from comienzo.forms import CrearFormulario, BuscarFormulario

def comienzo(request):
    return render(request,"comienzo/index.html")

def template1(request):
     return render(request,"template1.html")

def acerca_de_mi(request):
    return render(request,"comienzo/acerca_de_mi.html")


def buscar_acolchados(request):
    formulario=BuscarFormulario(request.GET)
    if formulario.is_valid():
        color=formulario.cleaned_data.get("color")
        composicion=formulario.cleaned_data.get("composicion")
        acolchados=Acolchados.objects.filter(color__icontains=color,composicion__icontains=composicion)
    return render(request,"comienzo/buscar_acolchados.html", {"acolchados":acolchados,"form":formulario})
    
def crear_acolchados(request):
    formulario=CrearFormulario()
    if request.method=="POST":
        formulario= CrearFormulario(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            acolchados=Acolchados(tamanio=data.get("tamanio"),color=data.get("color"),composicion=data.get("composicion"))
            acolchados.save()
            return redirect("comienzo:crear_acolchados")
            
    return render(request,"comienzo/crear_acolchados.html", {"form":formulario})