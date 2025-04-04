from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Restaurante.forms import MesaForm
from Restaurante.models import Mesa

def mesa_list(request):
    mesas = Mesa.objects.all()
    return render(request, "restaurante/mesas/list.html", {"mesas": mesas})

def mesa_create(request):
    if request.method == "POST":
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mesa_list")
    else:
        form = MesaForm()
    return render(request, "restaurante/mesas/form.html", {"form": form})

def mesa_update(request, id):
    mesa = Mesa.objects.get(id=id)
    if request.method == "POST":
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect("mesa_list")
    else:
        form = MesaForm(instance=mesa)
    return render(request, "restaurante/mesas/form.html", {"form": form})

def mesa_delete(request, id):
    mesa = Mesa.objects.get(id=id)
    mesa.delete()
    return redirect("mesa_list")

