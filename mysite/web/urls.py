from django.urls import path
from . import views
#Hace falta revisión, rehacer código CRUD de mascotas si es necesario
urlpatterns = [
    path('', views.MascotaList.as_view(), name='mascota_list'),
    path('view/<int:pk>', views.MascotaView.as_view(), name='mascota_view'),
    path('new', views.MascotaCreate.as_view(), name='mascota_new'),
    path('edit/<int:pk>', views.MascotaUpdate.as_view(), name='mascota_edit'),
    path('delete/<int:pk>', views.MascotaDelete.as_view(), name='mascota_delete'),
]