from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventario
from .forms import InventarioForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

def lista_inventario(request):
    busqueda = request.GET.get("buscar", "")
    items = Inventario.objects.select_related("id_producto").all()
    if busqueda:
        items = items.filter(Q(id_producto__nombre__icontains=busqueda))
    items = items.order_by("id_producto__nombre")
    paginador = Paginator(items, 10)
    numero_pagina = request.GET.get("page")
    items = paginador.get_page(numero_pagina)
    return render(request, "inventario/lista.html", {
        "items": items,
        "busqueda": busqueda
    })

def editar_inventario(request, id_inventario):
    item = get_object_or_404(Inventario, pk=id_inventario)
    if request.method == "POST":
        formulario = InventarioForm(request.POST, instance=item)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Inventario actualizado correctamente.")
            return redirect("lista_inventario")
    else:
        formulario = InventarioForm(instance=item)
    return render(request, "inventario/editar.html", {
        "formulario": formulario,
        "titulo": "Editar Inventario"
    })

def eliminar_inventario(request, id_inventario):
    item = get_object_or_404(Inventario, pk=id_inventario)
    if request.method == "POST":
        item.delete()
        messages.success(request, "Registro de inventario eliminado.")
        return redirect("lista_inventario")
    return render(request, "inventario/eliminar.html", {"item": item})