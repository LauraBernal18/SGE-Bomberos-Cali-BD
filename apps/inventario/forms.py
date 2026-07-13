from django import forms
from .models import Inventario

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ["stock_actual", "stock_minimo", "demanda_diaria", "estado_stock", "id_producto"]
        widgets = {
            "stock_actual": forms.NumberInput(attrs={"class": "form-control"}),
            "stock_minimo": forms.NumberInput(attrs={"class": "form-control"}),
            "demanda_diaria": forms.NumberInput(attrs={"class": "form-control"}),
            "estado_stock": forms.Select(
                choices=[("Seguro", "Seguro"), ("Alerta", "Alerta"),
                         ("Crítico", "Crítico"), ("Agotado", "Agotado")],
                attrs={"class": "form-select"}
            ),
            "id_producto": forms.Select(attrs={"class": "form-select"}),
        }