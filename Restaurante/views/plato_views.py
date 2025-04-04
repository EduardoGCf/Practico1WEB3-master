from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Restaurante.forms import PlatoForm
from Restaurante.models import Plato

def plato_list(request):
    platos = Plato.objects.all()
    return render(request, "restaurante/platos/list.html", {"platos": platos})

def plato_create(request):
    if request.method == "POST":
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("plato_list")
    else:
        form = PlatoForm()
    return render(request, "restaurante/platos/form.html", {"form": form})

def plato_update(request, id):
    plato = Plato.objects.get(id=id)
    if request.method == "POST":
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect("plato_list")
    else:
        form = PlatoForm(instance=plato)
    return render(request, "restaurante/platos/form.html", {"form": form})

def plato_delete(request, id):
    plato = Plato.objects.get(id=id)
    plato.delete()
    return redirect("plato_list")


