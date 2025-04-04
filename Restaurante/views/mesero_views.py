from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Restaurante.forms import MeseroForm
from Restaurante.models import Mesero

def mesero_list(request):
    meseros = Mesero.objects.all()
    return render(request, "restaurante/meseros/list.html", {"meseros": meseros})

def mesero_create(request):
    if request.method == "POST":
        form = MeseroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mesero_list")
    else:
        form = MeseroForm()
    return render(request, "restaurante/meseros/form.html", {"form": form})

def mesero_update(request, id):
    mesero = Mesero.objects.get(id=id)
    if request.method == "POST":
        form = MeseroForm(request.POST, instance=mesero)
        if form.is_valid():
            form.save()
            return redirect("mesero_list")
    else:
        form = MeseroForm(instance=mesero)
    return render(request, "restaurante/meseros/form.html", {"form": form})

def mesero_delete(request, id):
    mesero = Mesero.objects.get(id=id)
    mesero.delete()
    return redirect("mesero_list")

