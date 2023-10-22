
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
   path('', inicio, name='Inicio'),
   path('aboutMe', aboutMe, name='AboutMe'),
   path('buscar/', buscarCafeterias, name='Buscar'),
   path('valoranos/', valoranos, name='Valoranos'),
   path('login/', login_request, name='Login'),
   path('register/', register, name='Register'),
   path('editarPerfil/', editarPerfil, name='EditarPerfil'),
   path('postAgregar/', postAgregar, name = "PostAgregar"),
]


#URLs de CBV
urlpatterns += [
   path('lista/', CafeteriaListView.as_view(), name="ListaCafeterias"),
   path('detalle/<int:pk>/', CafeteriaDetailView.as_view(), name="DetalleCafeteria"),
   path('editar/<int:pk>/', CafeteriaEditarView.as_view(), name = "EditarCafeteria"),
   path('eliminar/<int:pk>/', CafeteriaDeletelView.as_view(), name = "EliminarCafeteria"),
   path('agregar/', CafeteriaAgregarView.as_view(), name = "AgregarCafeteria"),
   path('perfil/<int:pk>', UsuarioDetailView.as_view(), name="Perfil"),
   path ('logout/', LogoutView.as_view(template_name = "App1/logout.html"), name="Cerrar sesion"), 
   
]
