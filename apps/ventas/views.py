from django.shortcuts import render, redirect, get_object_or_404
from .models import Orden
from .forms import OrdenForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.db import connection

def lista_ventas(request):
    busqueda = request.GET.get("buscar", "")
    ordenes = Orden.objects.select_related("id_cliente", "id_empleado", "id_sede").all()
    if busqueda:
        ordenes = ordenes.filter(
            Q(id_cliente__nombre_razon_social__icontains=busqueda) |
            Q(estado__icontains=busqueda)
        )
    ordenes = ordenes.order_by("-fecha")
    paginador = Paginator(ordenes, 10)
    numero_pagina = request.GET.get("page")
    ordenes = paginador.get_page(numero_pagina)
    return render(request, "ventas/lista.html", {
        "ordenes": ordenes,
        "busqueda": busqueda
    })

def crear_venta(request):
    if request.method == "POST":
        formulario = OrdenForm(request.POST)
        if formulario.is_valid():

            with connection.cursor() as cursor:
                cursor.execute("""
                               SELECT setval(pg_get_serial_sequence('orden', 'id_orden'),
                                             COALESCE(MAX(id_orden), 1))
                               FROM orden;
                               """)
            formulario.save()
            messages.success(request, "Orden registrada correctamente.")
            return redirect("lista_ventas")
    else:
        formulario = OrdenForm()
    return render(request, "ventas/crear.html", {
        "formulario": formulario,
        "titulo": "Nueva Orden"
    })

def editar_venta(request, id_orden):
    orden = get_object_or_404(Orden, pk=id_orden)
    if request.method == "POST":
        formulario = OrdenForm(request.POST, instance=orden)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Orden actualizada correctamente.")
            return redirect("lista_ventas")
    else:
        formulario = OrdenForm(instance=orden)
    return render(request, "ventas/editar.html", {
        "formulario": formulario,
        "titulo": "Editar Orden"
    })

def eliminar_venta(request, id_orden):
    orden = get_object_or_404(Orden, pk=id_orden)
    if request.method == "POST":
        orden.delete()
        messages.success(request, "Orden eliminada correctamente.")
        return redirect("lista_ventas")
    return render(request, "ventas/eliminar.html", {"orden": orden})