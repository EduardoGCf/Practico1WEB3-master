from django import forms

from Restaurante.models import Mesero

class MeseroForm(forms.ModelForm):
    nombres = forms.CharField(
        label="Nombres",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    apellidos = forms.CharField(
        label="Apellidos",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    telefono = forms.IntegerField(
        label="Telefono",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    class Meta:
        model = Mesero
        fields = ["nombres", "apellidos", "telefono"]