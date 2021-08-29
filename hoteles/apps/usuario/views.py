from django.shortcuts import render
from django.http import HttpResponseRedirect
#vamos a importar una vista que esta preparada para trabajar con formularios 
from django.views.generic.edit import CreateView, FormView
#importo el formulario que hemos creado
from apps.usuario.forms import FormularioLogin, FormularioUsuario 
#vamos a hacer que no se almacene en cache la infromacion,  proteccio de crosfire para ecitar algunas vulneraciones comunes que son conocidas e el mundo web
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout

from apps.usuario.models import Usuario


#hdevueve una vista si todo ha terminado correcto.
from django.urls import reverse_lazy

#vamos a crear una clase que herede de FromViews
class Login(FormView):
    template_name='login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    #usamos los decoradores para proteger que la informacion no se almacene en cache y para algunas bunerabilidades que yas econocen en el mundo web
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    #vamos a llamar a la clase padre view de la cual hereda todas las vistadas basadas en clases. redefinimos dispach que es quien mira el tipo de peticion GET, POST..

    def dispatch(self,request,*args,**kwargs):
        #si el ususario esta logeado lo redireccionamos a success_url
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)


    def form_valid(self,form):
        #meto en login el usuario que nos interesa
        
        login(self.request,form.get_user())
        #devuelvo un form valido
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class RegistrarUsusario(CreateView):
    model = Usuario
    template_name = 'registrarUsuario.html'
    form_class = FormularioUsuario
    success_url = reverse_lazy('index')

    
