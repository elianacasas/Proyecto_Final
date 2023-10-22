from django import forms
from .models import Cafeterias, Comentario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


 
 
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, label="Nombre")
    last_name = forms.CharField(max_length=20, label="Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label="Constraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, label="Modificar nombre", required=False)
    last_name = forms.CharField(max_length=20, label="Modificar apellido", required=False)
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Constraseña nueva", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput, required=False)
    imagen = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class AgregarFormulario(forms.ModelForm):
    class Meta:
        model = Cafeterias
        fields = ['name', 'direccion', 'horario', 'descripcion']
    
    
class BuscarCafeterias(forms.Form):
    direccion = forms.CharField()

class ReseñaFormulario(forms.Form):
    name = forms.CharField()
    opinion = forms.CharField()
    puntaje = forms.IntegerField()

class UpdateFormulario(forms.ModelForm):
      class Meta:
        model = Cafeterias
        fields = ['name', 'direccion', 'horario', 'descripcion', 'imagen']
        
class ComentarioForm(forms.ModelForm):
   
    class Meta:
        model = Comentario
        fields = ['contenido']

    
    