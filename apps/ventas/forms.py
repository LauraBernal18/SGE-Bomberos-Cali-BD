from django import forms
from .models import Orden

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ["fecha", "total", "estado", "observaciones", "id_cliente", "id_empleado", "id_sede"]
        widgets = {
            "fecha": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "total": forms.NumberInput(attrs={"class": "form-control"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
            "observaciones": forms.TextInput(attrs={"class": "form-control"}),
            "id_cliente": forms.Select(attrs={"class": "form-select"}),
            "id_empleado": forms.Select(attrs={"class": "form-select"}),
            "id_sede": forms.Select(attrs={"class": "form-select"}),
        }