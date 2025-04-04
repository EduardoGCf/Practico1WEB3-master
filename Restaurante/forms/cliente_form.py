from django import forms

from Restaurante.models import Cliente

class ClienteForm(forms.ModelForm):
    nombres = forms.CharField(
        label="Nombres",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    nit = forms.CharField(
        label="NIT",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    class Meta:
        model = Cliente
        fields = ["nombres", "nit"]
