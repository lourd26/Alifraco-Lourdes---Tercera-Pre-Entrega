from django import forms 

class CrearFormulario(forms.Form):
    TAMAÑO_CHOICES = [
        ("twin", "Twin"),
        ("queen", "Queen"),
        ("king", "King")
        ]

    tamanio=forms.ChoiceField(choices=TAMAÑO_CHOICES,label="Tamaño")
    color=forms.CharField(max_length=20)
    composicion=forms.CharField(max_length=20)
    fecha_fabricacion=forms.DateField()
    imagen_acolchado=forms.ImageField(required=False)

class BuscarFormulario(forms.Form):
    color=forms.CharField(max_length=20,required=False)
    composicion=forms.CharField(max_length=20,required=False)


class EditarFormulario(forms.Form):
    TAMAÑO_CHOICES = [
        ("twin", "Twin"),
        ("queen", "Queen"),
        ("king", "King")
        ]

    tamanio=forms.ChoiceField(choices=TAMAÑO_CHOICES,label="Tamaño")
    color=forms.CharField(max_length=20)
    composicion=forms.CharField(max_length=20)
    fecha_fabricacion=forms.DateField()
    imagen_acolchado=forms.ImageField(required=False)
