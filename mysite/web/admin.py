from django.contrib import admin
from .models import Perfil, Mascota
# Register your models here.

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rut', 'nombres', 'apellidos', 'nacimiento', 'telefono', 'email')

admin.site.register(Mascota)