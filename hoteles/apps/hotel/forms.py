from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from ckeditor.fields import RichTextField
from django.forms import widgets

from apps.hotel.models import Comentario, Hotel


class FormRegisterHotel(forms.ModelForm): 

    
    class Meta:
        model = Hotel
        fields = ['nombre', 'telefono', 'pais', 'comunidad',
         'ciudad','direccion','correo','descripcionRapida', ]
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Nombre del Hotel',
                }
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : "Telefono",
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "Pais"
                }
            ),
            'comunidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "Comunidad"
                }
            ),
            'ciudad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "Ciudad"
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "Direccion"
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "CorreoElectronico"
                }
            ),
            'cominidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "username"
                }
            ),
            'descripcionRapida': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "Descripcion Rapida"
                }
            ),
            
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields={'nombre', 'comentario'}
        widgets={
            'comentario': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "Comentario",
                    'rows':8, 'cols':15,
                    'rezice': None
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Nombre'
                }
            )

        }