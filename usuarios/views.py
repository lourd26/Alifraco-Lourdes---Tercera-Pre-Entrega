from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate,login
from usuarios.forms import FormularioDeRegistro,FormularioModificarPerfil,FormularioModificarContrasenia
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from usuarios.models import DatosExtra

def acceso(request):
    formulario=AuthenticationForm()
    if request.method == "POST":
        formulario=AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            nombre_usuario=formulario.cleaned_data.get("username")
            contrasenia=formulario.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario,password=contrasenia)
            
            login(request,usuario)
            DatosExtra.objects.get_or_create(user=usuario)
            return redirect("comienzo:inicio")
        
    
    return render(request,"usuarios/acceso.html",{"form":formulario})

def registro(request):
    formulario=FormularioDeRegistro()
    if request.method=="POST":
        formulario=FormularioDeRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("usuarios:acceso")
    return render(request,"usuarios/registro.html",{"form":formulario})

@login_required
def modificar_perfil(request):
    datos_extra=request.user.datosextra
    formulario=FormularioModificarPerfil(instance=request.user,initial={"avatar":datos_extra.avatar})
    if request.method=="POST":
        formulario=FormularioModificarPerfil(request.POST,request.FILES,instance=request.user)
        if formulario.is_valid():
            new_avatar=formulario.cleaned_data.get("avatar")
            datos_extra.avatar=new_avatar if new_avatar else datos_extra.avatar
            datos_extra.save()
            formulario.save()
            return redirect("usuarios:acceso")
    return render(request,"usuarios/modificar_perfil.html",{"form":formulario})

class ModificarContrasenia(LoginRequiredMixin,PasswordChangeView):
    form_class=FormularioModificarContrasenia
    template_name="usuarios/modificar_contrasenia.html"
    success_url=reverse_lazy("usuarios:modificar_perfil")
