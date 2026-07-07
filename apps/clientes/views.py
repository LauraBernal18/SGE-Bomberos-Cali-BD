from django.shortcuts import render, redirect, get_object_or_404

from .models import Cliente
from .forms import ClienteForm


def lista_clientes(request):
    clientes = Cliente.objects.all().order_by("nombre_razon_social")

    return render(
        request,
        "clientes/lista.html",
        {"clientes": clientes}
    )


def crear_cliente(request):

    if request.method == "POST":

        formulario = ClienteForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("lista_clientes")

    else:

        formulario = ClienteForm()

    return render(
        request,
        "clientes/formulario.html",
        {"formulario": formulario}
    )


def editar_cliente(request, id_cliente):

    cliente = get_object_or_404(
        Cliente,
        pk=id_cliente
    )

    if request.method == "POST":

        formulario = ClienteForm(
            request.POST,
            instance=cliente
        )

        if formulario.is_valid():

            formulario.save()

            return redirect("lista_clientes")

    else:

        formulario = ClienteForm(instance=cliente)

    return render(
        request,
        "clientes/formulario.html",
        {
            "formulario": formulario,
            "titulo": "Editar Cliente"
        }
    )

def eliminar_cliente(request, pk):

        cliente = get_object_or_404(Cliente, pk=pk)

        if request.method == "POST":

            cliente.delete()

            return redirect("lista_clientes")

        return render(
            request,
            "clientes/eliminar.html",
            {"cliente": cliente}
        )