from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Restaurante.forms import OrdenForm
from Restaurante.models import Orden, Cliente


def orden_list(request):
    ordenes = Orden.objects.all()
    return render(request, "restaurante/ordenes/list.html", {"ordenes": ordenes})


def orden_create(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            mesa = form.cleaned_data['mesa']
            form.save()
            return redirect('orden_list')
    else:
        form = OrdenForm()

    return render(request, 'restaurante/ordenes/form.html', {'form': form})
def orden_update(request, id):
    orden = Orden.objects.get(id=id)
    if request.method == "POST":
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect("orden_list")
    else:
        form = OrdenForm(instance=orden)
    return render(request, "restaurante/ordenes/form.html", {"form": form})

def orden_delete(request, id):
    orden = Orden.objects.get(id=id)
    orden.delete()
    return redirect("orden_list")


def orden_pagar(request, id):
    orden = get_object_or_404(Orden, id=id)
    if orden.estado != "En Proceso":
        return redirect('orden_list')

    clientes = Cliente.objects.all()

    if request.method == "POST":
        cliente_id = request.POST.get("cliente")
        if cliente_id:
            orden.cliente = Cliente.objects.get(id=cliente_id)
        orden.estado = "Cerrado"
        orden.save()
        return redirect('orden_list')

    return render(request, 'restaurante/ordenes/pagar_orden.html', {'orden': orden, 'clientes': clientes})