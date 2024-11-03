from django.urls import path
from comienzo.views import comienzo,acerca_de_mi,template1

app_name="comienzo"

urlpatterns = [
   path("",comienzo,name="inicio"),
   path("acerca-de-mi/",acerca_de_mi,name="acerca_de_mi"),
   path("template1/",template1,name="template1"),

]
