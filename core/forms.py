from django import forms
from .models import Estudiante, Enfermedad, Formulario, Retiro, Curso
from .models import Familia
from .models import Estudiante_Familia_Enfermedad_Formulario_Retiro

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['Nombre', 'Apellido', 'Sexo', 'Email', 'Edad' , 'Curso' , 'Cedula' , 'Direccion', 'Fecha_Nacimiento', 'N_de_Telefono' , 'Codigo_Matricula']

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ['Nombre_Madre','Nombre_Padre','Apellido_Padre','Apellido_Madre','Ocupacion_Padre','Ocupacion_Madre' , 'Trabaja_Donde_Madre','Trabaja_Donde_Padre','Estado_Civil_Madre','Estado_Civil_Padre', 'Vive_con_el_Niño_Madre','Vive_con_el_Niño_Padre','Telefonos_Madre','Telefonos_Padre','Direccion_Madre','Direccion_Padre','Instruccion_Madre','Instruccion_Padre','Tutor','Estudiante']

class EnfermedadForm(forms.ModelForm):
    class Meta:
        model = Enfermedad
        fields = ['Tipo','Explique','Estudiante']

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['Educacion_Formulario', 'Relacion_Formulario','Conducta_Formulario','Internet_Formulario', 'Transporte_Formulario','Estudiante']

class RetiroForm(forms.ModelForm):
    class Meta:
        model = Retiro
        fields = ['Nombre', 'Apellido', 'Edad', 'Cedula','Direccion','N_de_Telefono','Estudiante']


class Estudiante_Familia_Enfermedad_Formulario_RetiroForm(forms.ModelForm):
    class Meta:
        model = Estudiante_Familia_Enfermedad_Formulario_Retiro
        fields = ['estudiante', 'familia', 'enfermedad', 'formulario', 'retiro']

class CursoForm(forms.ModelForm):
        class Meta:
            model = Curso
            fields = [
                'nivel',
                'paralelo'
            ]
            labels = {
                'nivel': 'NIVEL',
                'paralelo': 'PARALELO'
            }
            widgets = {
                'nivel': forms.TextInput(attrs={'class': 'form-control'}),
                'paralelo': forms.TextInput(attrs={'class': 'form-control'}),
            }