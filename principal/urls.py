from django.urls import path
from principal import views
from .views import ExportToExcelView


urlpatterns = [
    path('',views.inicio, name='inicio'),#se buscar el views inicio, y su nombre
    path('login/', views.custom_login, name='custom_login'),
    path('contacto/', views.contacto, name='contacto'),
    path('cursos/', views.cursos, name='cursos'),
    path('Escuelas', views.Escuelas, name="Escuelas"),
    path('agregar-curso/', views.agregar_curso, name='agregar_curso'),
    path('listar-curso/', views.listar_cursos, name='listar_cursos'),
    path('modificar-curso/<id>', views.modificar_curso, name='modificar_curso'),   
    path('eliminar-curso/<id>', views.eliminar_curso, name='eliminar_curso'),     
    path('registro', views.registro, name='registro'),
    path('registro2', views.registro2, name='registro2'),
    path('asignar_docente/<int:curso_id>/', views.asignar_docente_a_curso, name='asignar_docente'),
    path('exportar-excel/', ExportToExcelView.as_view(), name='exportar_excel'),
]

