from django.contrib import admin
from .models import Curso, Contacto, Nota
from django import forms
from django.contrib.auth.models import User, Group
#from django.utils.html import format_html
# Register your models here.

class CursoAdminForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
#        exclude = ['estudiantes_inscritos']


    def __init__(self, *args, **kwargs):
        super(CursoAdminForm, self).__init__(*args, **kwargs)

        # Filtra los usuarios que pertenecen al grupo "Docente"
        docente_group = Group.objects.get(name='Docente')
        self.fields['docente'].queryset = User.objects.filter(groups=docente_group)

class CursoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "precio", "cupo", "docente"]
    list_editable = ["precio", "cupo"]
    search_fields = ["nombre"]
    list_filter = ["precio"]
    form = CursoAdminForm

class NotaAdmin(admin.ModelAdmin):
    list_display = '__all__'

admin.site.register(Curso, CursoAdmin)
admin.site.register(Nota)
admin.site.register(Contacto)
