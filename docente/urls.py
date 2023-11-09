from django.urls import path 
from . import views


urlpatterns = [
    path('cuenta/', views.cuenta2, name='cuenta_docente'),
    path('perfil/', views.perfil, name='perfil'),
    path('listar-curso/', views.lista_de_cursos2, name='lista_de_cursos'),
    path('cursos_asignados/', views.cursos_asignados, name='cursos_asignados'),
    path('estudiantes_inscritos/', views.estudiantes_inscritos, name='estudiantes_inscritos'),    
    path('ver-detalles-estudiante/<int:user_id>/', views.ver_detalles_estudiante, name='ver_detalles_estudiante'),
#    path('editar-nota/<int:curso_id>/', views.editar_nota, name='editar_nota'),
    path('editar-nota/<int:nota_id>/', views.editar_nota, name='editar_nota'),
    path('exportar-excel/', views.exportar_a_excel, name='exportar_excel'),
]