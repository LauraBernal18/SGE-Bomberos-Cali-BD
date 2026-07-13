from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_ventas, name="lista_ventas"),
    path("nueva/", views.crear_venta, name="crear_venta"),
    path("editar/<int:id_orden>/", views.editar_venta, name="editar_venta"),
    path("eliminar/<int:id_orden>/", views.eliminar_venta, name="eliminar_venta"),
]