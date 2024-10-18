from django import forms 

class CrearFormulario(forms.Form):
    tamanio=forms.CharField(max_length=20)
    color=forms.CharField(max_length=20)
    composicion=forms.CharField(max_length=20)

class BuscarFormulario(forms.Form):
    color=forms.CharField(max_length=20,required=False)
    composicion=forms.CharField(max_length=20,required=False)
