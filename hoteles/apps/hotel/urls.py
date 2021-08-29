from django.urls import path

from apps.hotel import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('crearHotel/',login_required(views.createHotel), name = 'crearhotel'),
    path('<int:hotel_id>/postHotel', views.PostHotel, name='postHotel'),
    path('buscarHoteles', views.buscrHoteles, name='buscarhotel')
]