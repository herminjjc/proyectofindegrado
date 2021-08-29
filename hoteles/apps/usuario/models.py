from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self,username,email,nombres,password=None):
        if not email:
            raise ValueError("el usuario no tiene email es obligatorio")
        
        usuario = self.model(
            username=username,
            email = self.normalize_email(email),
            nombres = nombres,
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self, username, email,nombres, password):
        usuario = self.create_user(
            username=username,
            email=email,
            nombres=nombres,
            password = password,
        )
        usuario.is_admin = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario',unique = True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254,unique = True)
    nombres = models.CharField('Nombres', max_length=200, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length=200,blank = True, null = True)
    imagen = models.ImageField('Imagen de Perfil', max_length=200,blank = True,null = True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    objects = UsuarioManager()


    #vamos a definir el parametro unico de quien es el que requiere para iniciar secion
    USERNAME_FIELD = 'username'

    # datos requeridos si o si  para crear a los superusuarios por el cmd(terminal)
    REQUIRED_FIELDS = ['email', "nombres"]

    def __str__(self):
        return f'{self.id},{self.nombres}'

    #vamos a definir un methodo hass_param() se define para ver quien puede aparecer 
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
 
    
    @property
    def is_staff(self):
        return self.is_admin