from django.db import models
from django.db.models.fields import NullBooleanField

from apps.usuario.models import Usuario
from ckeditor.fields import RichTextField

# Create your models here.


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre Hotel", max_length= 200, null=False, blank=True, default="")
    telefono= models.IntegerField("telefono")
    pais = models.CharField("Pais",max_length=100)
    comunidad = models.CharField("Comunidad", max_length= 200, null=False, blank=True, default="")
    ciudad = models.CharField("Ciudad",max_length=100)
    direccion = models.CharField("Direccion", max_length= 200, null=False, blank=True, default="")
    correo = models.EmailField("correo")
    descripcionRapida = models.TextField("Descripcion rapida", default="")
    
    #establecemos las relaciones que vamos a poner
    usuario  = models.ForeignKey(Usuario,on_delete = models.CASCADE)

    #establecemos las relaciones que tiene con la anterior tambla

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"

    def __str__(self):
        return self.nombre
    


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length= 200, null=False, blank=True, default="")
    comentario = models.TextField("comentario")
    sentiment = models.BooleanField('sentiment')

    #establecemos las relaciones que vamos a poner
    hotel  = models.ForeignKey(Hotel,on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.comentario
