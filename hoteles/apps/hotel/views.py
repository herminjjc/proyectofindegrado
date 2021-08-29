from apps import hotel
from django.views import generic
from django.views.generic.base import View

from apps.hotel.models import Hotel
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from apps.hotel.forms import FormRegisterHotel,ComentarioForm
from django.http import HttpResponse, response,HttpResponseRedirect

from django.urls import reverse

from .service import get_sentiment

# Create your views here.


class Inicio(generic.ListView):
    model = Hotel
    context_object_name = 'hotels'
    queryset = Hotel.objects.all()
    template_name = 'index.html'
    
    





def createHotel(request):
    
    if request.method == 'POST':
        hotel_form= FormRegisterHotel(request.POST)
        print(request.user)
        if hotel_form.is_valid():  # valido los datos enviados con la funcion de django
            print(request.user)
            hotel = hotel_form.save(commit=False)  # registro en mi base de datos.
            hotel.usuario = request.user
            hotel.save()
            # redirecciono a index que es el nombre que he puesto en url.
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'registrarHotel.html', {'form': hotel_form})
            
    else:
        hotel_form= FormRegisterHotel()
    return render(request, 'registrarHotel.html', {'form': hotel_form})


def PostHotel(request, hotel_id):
    hotel = get_object_or_404(Hotel,pk = hotel_id)
    if request.method == 'POST':
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            comentario= form_comentario.save(commit=False)
            comentario.hotel=hotel
            comentario.sentiment= get_sentiment(comentario.comentario)
            comentario.save()
            return HttpResponseRedirect(reverse('hotel:postHotel', args=(hotel.id,)))
        else:
            return render(request, 'postHotel.html', {'hotel': hotel, 'form': form_comentario})

    else:
        form_comentario = ComentarioForm()
        comentariospos = hotel.comentario_set.filter(sentiment= True).count()
        if comentariospos !=0:
            satisfaction = round(( comentariospos * 100)/ hotel.comentario_set.count(), 2)
        else:
            comentariosneg =  hotel.comentario_set.filter(sentiment= False).count()
            print(comentariosneg)
            if comentariosneg !=0:
                satisfaction =  - round(( comentariosneg * 100)/ hotel.comentario_set.count(), 2)
                print(satisfaction)
            else:
                satisfaction =0 

        return render(request, 'postHotel.html', {'hotel': hotel, 'form': form_comentario,'satisfaction': satisfaction})


def buscrHoteles(request):

    if request.method == 'POST':
        filtro = request.POST['search']
        hotels = Hotel.objects.filter(ciudad= filtro)
        print (hotels)
        return render(request, 'index.html', {'hotels': hotels})
    else:
        hotels = Hotel.objects.all()
        return render(request, 'index.html', {'hotels': hotels})

