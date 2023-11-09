from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.core.validators import MaxValueValidator
# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()
    cupo = models.PositiveIntegerField()
    estudiantes_inscritos = models.ManyToManyField(User, related_name='cursos_inscritos', blank=True)
    cantidad_estudiantes = models.PositiveIntegerField(default=0)  # Nuevo campo para la cantidad de estudiantes
    docente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='cursos_docente')

    def __str__ (self): #esto para devolver el campo que mas lo represente
        return self.nombre
    
class Nota(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, validators=[MaxValueValidator(100)])

    def __str__(self):
        return f"{self.estudiante.username} - {self.curso.nombre}"    
    
opciones_consultas = [
    [0, "Consulta"],
    [1, "Reactivacion de cuenta"],
    [2, "Sugerencia"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
    
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dpi = models.CharField(max_length=13, blank=True)    
    telefono = models.CharField(max_length=15, blank=True)
    fecha = models.DateField(null=True, blank=True)    

    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)