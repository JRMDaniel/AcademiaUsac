from django.shortcuts import render, redirect, get_object_or_404
from principal.models import Curso, Nota
from django.contrib.auth.decorators import login_required
# Create your views here.


def cuenta(request):#cuenta de estudiante
    user_belongs_to_estudiante_group = request.user.groups.filter(name='Estudiante').exists()
    user_belongs_to_docente_group = request.user.groups.filter(name='Docente').exists()
    context = {
        'user_belongs_to_estudiante_group': user_belongs_to_estudiante_group,
        'user_belongs_to_docente_group': user_belongs_to_docente_group,
    }
    return render(request, 'student/cuenta.html', context)

def perfil(request):#ver el perfil del usuario 
    usuario = request.user
    grupos_del_usuario = usuario.groups.all()
    contexto = {
        'usuario': usuario,
        'grupos_del_usuario': grupos_del_usuario,
    }
    return render(request, 'student/perfil.html', contexto)

def cursos_estudiante(request):
    cursos = Curso.objects.all()
    for curso in cursos:
        # Calcula la cantidad de cupos disponibles restando la cantidad de estudiantes inscritos al cupo total
        curso.cupos_disponibles = curso.cupo - curso.cantidad_estudiantes
    data = {
        'cursos': cursos
    }
    return render(request, 'student/lista_cursos.html', data)

@login_required
def inscribirse_a_curso(request, curso_id):#para poder inscribirse al curso
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        # Aquí maneja la inscripción del usuario en el curso
        user = request.user  # Obtén el usuario actual
        if user not in curso.estudiantes_inscritos.all():
            curso.estudiantes_inscritos.add(user)  # Agrega el usuario al campo ManyToManyField
            curso.cantidad_estudiantes += 1  # Incrementa la cantidad de estudiantes
            curso.save()  # Guarda la actualización en la base de datos
        return redirect('cursos_estudiante')
    return redirect('cursos_estudiante')

def cursos_del_usuario(request):#Para obtener los cursos a los que el usuario actual está inscrito
    cursos_inscritos = Curso.objects.filter(estudiantes_inscritos=request.user)
    data = {
        'cursos_inscritos': cursos_inscritos
    }
    return render(request, 'student/cursos_del_usuario.html', data)

def eliminar_inscripcion(request, curso_id):#Para que el estudiante elimine el curso al que se ha asignado
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        user = request.user  # Obtén el usuario actual
        if user in curso.estudiantes_inscritos.all():
            curso.estudiantes_inscritos.remove(user)
            curso.cantidad_estudiantes -= 1
            curso.save()
        return redirect('cursos_estudiante')
    return redirect('cursos_estudiante')

def detalle_curso(request, curso_id):#para que el estudiante pueda ver los detalles del curso en una sola pagina
    # Obtén el curso específico usando el parámetro curso_id
    curso = get_object_or_404(Curso, id=curso_id)
    estudiante = request.user  # El usuario actual
    nota = Nota.objects.filter(estudiante=estudiante, curso=curso).first()
    # A continuación, puedes pasar el objeto 'curso' a una plantilla para mostrar sus detalles
    return render(request, 'student/detalle_curso.html', {'curso': curso, 'nota':nota})