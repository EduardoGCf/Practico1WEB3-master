from django.urls import path

from . import views

urlpatterns = [
    path("", views.orden_list, name="orden_list"),
    path("hola", views.hola, name="hola"),
    path("plato/create", views.plato_create, name="plato_create"),
    path("plato", views.plato_list, name="plato_list"),
    path("plato/<int:id>", views.plato_update, name="plato_edit"),
    path("plato/delete/<int:id>", views.plato_delete, name="plato_delete"),

    path("clientes/create", views.cliente_create, name="cliente_create"),
    path("clientes", views.cliente_list, name="cliente_list"),
    path("clientes/<int:id>", views.cliente_update, name="cliente_edit"),
    path("clientes/delete/<int:id>", views.cliente_delete, name="cliente_delete"),

    path("mesero/create", views.mesero_create, name="mesero_create"),
    path("mesero", views.mesero_list, name="mesero_list"),
    path("mesero/<int:id>", views.mesero_update, name="mesero_edit"),
    path("mesero/delete/<int:id>", views.mesero_delete, name="mesero_delete"),

    path("mesa/create", views.mesa_create, name="mesa_create"),
    path("mesa", views.mesa_list, name="mesa_list"),
    path("mesa/<int:id>", views.mesa_update, name="mesa_edit"),
    path("mesa/delete/<int:id>", views.mesa_delete, name="mesa_delete"),


    path("orden/create", views.orden_create, name="orden_create"),
    path("orden", views.orden_list, name="orden_list"),
    path("orden/<int:id>", views.orden_update, name="orden_edit"),
    path("orden/delete/<int:id>", views.orden_delete, name="orden_delete"),
    path("orden/pagar/<int:id>", views.orden_pagar, name="orden_pagar"),
]
