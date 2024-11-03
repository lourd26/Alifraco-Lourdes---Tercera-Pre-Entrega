from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User

class FormularioDeRegistro(UserCreationForm):
    username=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput)
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    
    class Meta:
        model=User
        fields=["username","email","password1","password2","first_name","last_name"]
        help_text={key:"" for key in fields}


class FormularioModificarContrasenia(PasswordChangeForm):
    old_password=forms.CharField(label="Contraseña actual",widget=forms.PasswordInput)
    new_password1=forms.CharField(label="Contraseña nueva",widget=forms.PasswordInput)
    new_password2=forms.CharField(label="Repetir contraseña nueva",widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=["old_password","new_password1","new_password2"]
        help_text={
            "old_password": "",
            "new_password1": "",
            "new_password2": "",
        }
        

class FormularioModificarPerfil(UserChangeForm):
    email=forms.EmailField(required=True)
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    password=None
    avatar=forms.ImageField(required=False)
    
    class Meta:
        model=User
        fields=["email","first_name","last_name","avatar"]
        help_text={key:"" for key in fields}