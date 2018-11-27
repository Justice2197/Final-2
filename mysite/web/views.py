from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil, Mascota
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
# Create your views here.

class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm
    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        rut = form.cleaned_data.get('rut')
        nombres = form.cleaned_data.get('nombres')
        apellidos = form.cleaned_data.get('apellidos')
        nacimiento = form.cleaned_data.get('nacimiento')
        telefono = form.cleaned_data.get('telefono')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username = usuario, password=password)
        login(self.request, usuario)
        obj = Perfil.objects.create(rut = rut,
        nombres = nombres,
        apellidos = apellidos,
        nacimiento = nacimiento,
        telefono = telefono,
        email = email)
        return render(request, 'web/MisPerris.html', {})

class BienvenidaView(TemplateView):
    template_name = 'web/MisPerris.html'

class SignInView(LoginView):
    template_name = 'web/iniciar_sesion.html'

class SignOutView(LogoutView):
    pass

class InfoView(TemplateView):
    template_name = 'web/quienes_somos.html'

class ContactView(TemplateView):
    template_name = 'web/contactanos.html'

class ServicioView(TemplateView):
    template_name = 'web/servicios.html'


class MascotaList(ListView):
    model = Mascota

class MascotaView(DetailView):
    model = Mascota

class MascotaCreate(CreateView):
    model = Mascota
    fields = ['nombre', 'raza', 'descripcion', 'estado']
    success_url = reverse_lazy('mascota_list')

class MascotaUpdate(UpdateView):
    model = Mascota
    fields = ['nombre', 'raza', 'descripcion', 'estado']
    success_url = reverse_lazy('mascota_list')

class MascotaDelete(DeleteView):
    model = Mascota
    success_url = reverse_lazy('mascota_list')

