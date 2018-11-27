from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Perfil

class SignUpForm(UserCreationForm):
    rut = forms.CharField(max_length=9, required=True)
    nombres = forms.CharField(max_length=50, required=True)
    apellidos = forms.CharField(max_length=50, required=True)
    nacimiento = forms.DateField(required=True)
    telefono = forms.CharField(max_length=12, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'rut',
            'nombres',
            'apellidos',
            'nacimiento',
            'telefono',
            'email',
            'password1',
            'password2'
        )


