from django.urls import path 
from . import views
 
urlpatterns = [
    path('cuenta/', views.cuenta, name='cuenta'),
    path('perfil/', views.perfil, name='perfil'),
    path('cursos/', views.cursos_estudiante, name='cursos_estudiante'),
    path('inscribir-a-curso/<int:curso_id>/', views.inscribirse_a_curso, name='inscribirse_a_curso'),
    path('mis-cursos/', views.cursos_del_usuario, name='cursos_del_usuario'),
    path('eliminar-inscripcion/<int:curso_id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
    path('detalle-curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
]