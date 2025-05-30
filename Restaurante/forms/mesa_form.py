from django import forms

from Restaurante.models import Mesa

class MesaForm(forms.ModelForm):
    numero = forms.IntegerField(
        label="Numero",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    class Meta:
        model = Mesa
        fields = ["numero"]