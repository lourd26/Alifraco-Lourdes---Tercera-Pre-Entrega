from django.urls import path
from comienzo.views import comienzo,acerca_de_mi,template1,crear_acolchados,buscar_acolchados

app_name="comienzo"

urlpatterns = [
   path("",comienzo,name="inicio"),
   path("acerca-de-mi/",acerca_de_mi,name="acerca_de_mi"),
   path("template1/",template1,name="template1"),
   path("buscar-acolchados/",buscar_acolchados,name="buscar_acolchados"),
   path("crear-acolchados/",crear_acolchados,name="crear_acolchados"),

    
]
