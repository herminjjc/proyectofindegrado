from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.usuario.models import Usuario

class FormularioLogin(AuthenticationForm):
    #redifino la clase init que tiene todo documento de paython sel, argumento y kwars, esto es 

    def __init__(self,*args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        #vamos a definir las propiedades que tiene la visata de html asignado las clases correspondientes
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Ususario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class FormularioUsuario(forms.ModelForm):
    """
    Formalutio de registro de un usuario en la base de datos
    """

    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model=Usuario
        #para especificar todos los campos
            #fields = {'__all__'}
        #para espicificar los campos que quiero
        fields={'email', 'username','nombres', 'apellidos' }
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Correo electronico',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Nombres',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "Aplellidos"
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "username"
                }
            )
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!= password2:
           raise forms.ValidationError('contraseñas no coinciden')
        return password2

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
