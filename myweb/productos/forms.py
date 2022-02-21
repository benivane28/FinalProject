from django import forms

class BusquedaProductos(forms.Form):
    servicio= forms.CharField(label='Servicio', max_length=60, required=True)