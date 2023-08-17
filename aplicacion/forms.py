from django import forms


class ProductoForm(forms.Form):
    nombre= forms.CharField(max_length=50, required=True)
    numero= forms.IntegerField(required=True)
    Cantidad = (
        (1, ""),
        (1, "Hay Stock (consultar cantidad)"),
        (1, "Sin stock"),
        )
    cantidad = forms.ChoiceField(label="Cantidad", choices=Cantidad, required=True)

class ClienteForm(forms.Form):
    nombre= forms.CharField(max_length=50, required=True)
    apellido= forms.CharField(max_length=50, required=True)
    email= forms.EmailField()

class ProveedorForm(forms.Form):
    nombre= forms.CharField(max_length=50, required=True)
    apellido= forms.CharField(max_length=50, required=True)
    email= forms.EmailField()
  
