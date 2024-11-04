from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name="usuarios"

urlpatterns = [
    path("acceso/",views.acceso,name="acceso"),
    path("registro/",views.registro,name="registro"),
    path("perfil/ver",views.ver_perfil,name="ver_perfil"),
    path("perfil/modificar",views.modificar_perfil,name="modificar_perfil"),
    path("perfil/modificar/contrasenia",views.ModificarContrasenia.as_view(),name="modificar_contrasenia"),
    path("salir/",LogoutView.as_view(template_name="usuarios/salir.html"),name="salir"),
    
    
]
