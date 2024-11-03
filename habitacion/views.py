from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from habitacion.models import Sabana,Frazada,Acolchados
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import Template,Context,loader
from django.shortcuts import render,redirect
from habitacion.forms import CrearFormulario, BuscarFormulario,EditarFormulario
from django.contrib.auth.decorators import login_required

#ACOLCHADO
def buscar_acolchados(request):
    formulario=BuscarFormulario(request.GET)
    if formulario.is_valid():
        color=formulario.cleaned_data.get("color")
        composicion=formulario.cleaned_data.get("composicion")
        acolchados=Acolchados.objects.filter(color__icontains=color,composicion__icontains=composicion)
    return render(request,"habitacion/buscar_acolchados.html", {"acolchados":acolchados,"form":formulario})
    
def crear_acolchados(request):
    formulario=CrearFormulario()
    if request.method=="POST":
        formulario= CrearFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            data=formulario.cleaned_data
            acolchados=Acolchados(tamanio=data.get("tamanio"),color=data.get("color"),composicion=data.get("composicion"),fecha_fabricacion=data.get("fecha_fabricacion"),imagen_acolchado=data.get("imagen_acolchado"))
            acolchados.save()
            return redirect("habitacion:buscar_acolchados")
            
    return render(request,"habitacion/crear_acolchados.html", {"form":formulario})

class VerAcolchados(DetailView):
    model= Acolchados
    template_name="habitacion/ver_acolchados.html"
    context_object_name="acolchado"


@login_required
def eliminar_acolchados(request,id):
    acolchados=Acolchados.objects.get(id=id)
    acolchados.delete()
    return redirect("habitacion:buscar_acolchados")

class EditarAcolchados(LoginRequiredMixin,UpdateView):
    model = Acolchados
    template_name = "habitacion/editar_acolchados.html"
    success_url=reverse_lazy("habitacion:buscar_acolchados")
    fields=["tamanio","color","composicion","fecha_fabricacion","imagen_acolchado"]
    context_object_name="acolchado"


#################################################################################3

#SABANA

class CrearSabana(CreateView):
    model = Sabana
    template_name = "habitacion/crear_sabana.html"
    success_url= reverse_lazy("habitacion:listado_sabanas")
    fields=["tamanio","color","composicion","hilos","fecha_fabricacion","imagen_sabana"]
    
class ListadoSabanas(ListView):
    model = Sabana
    template_name = "habitacion/listado_sabanas.html"
    context_object_name="sabanas"

class VerSabana(DetailView):
    model = Sabana
    template_name = "habitacion/ver_sabana.html"

class EditarSabana(LoginRequiredMixin,UpdateView):
    model = Sabana
    template_name = "habitacion/editar_sabana.html"
    success_url=reverse_lazy("habitacion:listado_sabanas")
    fields=["tamanio","color","composicion","hilos","fecha_fabricacion","imagen_sabana"]

class EliminarSabana(LoginRequiredMixin,DeleteView):
    model = Sabana
    template_name = "habitacion/eliminar_sabana.html"
    success_url=reverse_lazy("habitacion:listado_sabanas")

#######################################################################################3

#SABANA

class CrearFrazada(CreateView):
    model = Frazada
    template_name = "habitacion/crear_frazada.html"
    success_url= reverse_lazy("habitacion:listado_frazadas")
    fields=["tamanio","color","estilo","fecha_fabricacion","imagen_frazada"]
    
class ListadoFrazadas(ListView):
    model = Frazada
    template_name = "habitacion/listado_frazadas.html"
    context_object_name="frazadas"

class VerFrazada(DetailView):
    model = Frazada
    template_name = "habitacion/ver_frazada.html"

class EditarFrazada(LoginRequiredMixin,UpdateView):
    model = Frazada
    template_name = "habitacion/editar_frazada.html"
    success_url=reverse_lazy("habitacion:listado_frazadas")
    fields=["tamanio","color","estilo","fecha_fabricacion","imagen_frazada"]

class EliminarFrazada(LoginRequiredMixin,DeleteView):
    model = Frazada
    template_name = "habitacion/eliminar_frazada.html"
    success_url=reverse_lazy("habitacion:listado_frazadas")

