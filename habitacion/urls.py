from django.urls import path
from habitacion import views

app_name="habitacion"

urlpatterns = [
    path("buscar-acolchados/",views.buscar_acolchados,name="buscar_acolchados"),
    path("crear-acolchados/",views.crear_acolchados,name="crear_acolchados"),
    path("ver-acolchados/<int:pk>/",views.VerAcolchados.as_view(),name="ver_acolchados"),
    path("eliminar-acolchados/<int:id>/",views.eliminar_acolchados,name="eliminar_acolchados"),
    path("editar-acolchados/<int:pk>/",views.EditarAcolchados.as_view(),name="editar_acolchados"),
    path("sabana/crear/",views.CrearSabana.as_view(),name="crear_sabana"),
    path("sabanas/",views.ListadoSabanas.as_view(),name="listado_sabanas"),
    path("sabana/<int:pk>/",views.VerSabana.as_view(),name="ver_sabana"),
    path("sabana/<int:pk>/editar",views.EditarSabana.as_view(),name="editar_sabana"),
    path("sabana/<int:pk>/eliminar",views.EliminarSabana.as_view(),name="eliminar_sabana"),
    path("frazada/crear/",views.CrearFrazada.as_view(),name="crear_frazada"),
    path("frazadas/",views.ListadoFrazadas.as_view(),name="listado_frazadas"),
    path("frazada/<int:pk>/",views.VerFrazada.as_view(),name="ver_frazada"),
    path("frazada/<int:pk>/editar",views.EditarFrazada.as_view(),name="editar_frazada"),
    path("frazada/<int:pk>/eliminar",views.EliminarFrazada.as_view(),name="eliminar_frazada"),
]

