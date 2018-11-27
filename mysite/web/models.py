from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    rut = models.CharField(max_length=9)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacimiento = models.DateField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    
    def __str__(self):
        return self.usuario.username

def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario = instance)

def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()

    
class Mascota(models.Model):
        nombre = models.CharField(max_length=70)
        raza = models.CharField(max_length=70)
        descripcion = models.TextField()
        estado = models.CharField(max_length=50)
        
def __str__(self):
        return self.name

def get_absolute_url(self):
        return reverse('mascota_edit', kwargs={'pk': self.pk})