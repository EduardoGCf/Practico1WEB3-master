from django import forms

from Restaurante.models import Orden, Mesa

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['mesero', 'mesa', 'platos']
        widgets = {
            'platos': forms.CheckboxSelectMultiple(),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'mesero': forms.Select(attrs={'class': 'form-control'}),
            'mesa': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mesas_ocupadas = Orden.objects.filter(estado='En Proceso').values_list('mesa_id', flat=True)
        self.fields['mesa'].queryset = Mesa.objects.exclude(id__in=mesas_ocupadas)
