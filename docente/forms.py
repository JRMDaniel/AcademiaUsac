from django import forms
#from django.contrib.auth.models import User  # O el modelo de usuario que estés utilizando
from principal.models import Nota

class EditarNotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['valor']  # Agrega aquí cualquier otro campo de la nota que desees editar
