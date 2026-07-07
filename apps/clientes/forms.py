from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):

    TIPO_DOC = [
        ("CC", "Cédula de Ciudadanía"),
        ("CE", "Cédula de Extranjería"),
        ("NIT", "NIT"),
    ]

    TIPO_CLIENTE = [
        ("Persona", "Persona"),
        ("Empresa", "Empresa"),
    ]

    SI_NO = [
        (True, "Sí"),
        (False, "No"),
    ]

    tipo_doc = forms.ChoiceField(
        choices=TIPO_DOC,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    tipo_cliente = forms.ChoiceField(
        choices=TIPO_CLIENTE,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    habeas_data = forms.TypedChoiceField(
        choices=SI_NO,
        coerce=lambda x: x == "True",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:

        model = Cliente

        exclude = ["id_cliente"]

        widgets = {

            "num_doc": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "nombre_razon_social": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "telefono": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "correo": forms.EmailInput(attrs={
                "class": "form-control"
            }),

            "direccion_operativa": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "direccion_residencial": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "ciudad": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "representante_legal": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "regimen_tributario": forms.TextInput(attrs={
                "class": "form-control"
            }),

        }