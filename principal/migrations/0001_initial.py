# Generated by Django 4.2.5 on 2023-10-29 03:46
from django.contrib.auth.models import Group
from django.db import migrations, models

def create_groups(apps, schema_editor):
    Group.objects.create(name='Estudiantes')
    Group.objects.create(name='Docentes')


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('cupo', models.PositiveIntegerField()),
            ],
        ),
        migrations.RunPython(create_groups),#para crear los grupos        
    ]