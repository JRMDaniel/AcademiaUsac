from django import forms
from .models import Contacto, Curso #del archivo models se importa cantacto, curso
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
#        fields = ["nombre", "correo","tipo_consulta","avisos"]
        fields = '__all__'#para que se muestre todo 

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = '__all__'
        exclude = ['estudiantes_inscritos']

class CustormUserCreationForm(UserCreationForm):

    class Meta: 
        model = User 
        fields = [ 'first_name','last_name','username','email','password1','password2']

class AsignarDocenteForm(forms.ModelForm):
    docentes = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(groups__name='Docente'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Curso
        fields = ['docentes']