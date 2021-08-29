from django.contrib import admin

# Register your models here.

from apps.usuario.models import Usuario


#Con esta clase añadimos los valores que queremos que se muestren en el sitio de administracion
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombres','apellidos',"username"]

    


admin.site.register(Usuario, UsuarioAdmin)
