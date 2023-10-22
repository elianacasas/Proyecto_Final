from django.db import models
from django.contrib.auth.models import User


class Cafeterias(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    horario = models.CharField(max_length=20)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='cafeterias_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"
       
    
class Reseñas(models.Model):
    opinion = models.TextField()
    puntaje = models.IntegerField()
    
    
class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    cafeteria = models.ForeignKey('Cafeterias', on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)

    def __str__(self):
        return self.contenido