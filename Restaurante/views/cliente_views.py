from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Restaurante.forms import ClienteForm
from Restaurante.models import Cliente

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, "restaurante/clientes/list.html", {"clientes": clientes})

def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    else:
        form = ClienteForm()
    return render(request, "restaurante/clientes/form.html", {"form": form})

def cliente_update(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, "restaurante/clientes/form.html", {"form": form})

def cliente_delete(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("cliente_list")
