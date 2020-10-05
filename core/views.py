from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.shortcuts import render, HttpResponse, redirect
from core.forms import EstudianteForm
from core.models import Estudiante
from core.forms import FamiliaForm,EnfermedadForm,RetiroForm
from core.models import Familia,Enfermedad,Retiro
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from core.forms import CursoForm
from core.models import Curso

@login_required(None,"",'login')
def portada(request, plantilla="portada.html"):
    return render(request, plantilla);

@login_required(None,"",'login')
def MyV(request, plantilla="MyV.html"):
    return render(request, plantilla);


class crearcurso(PermissionRequiredMixin,CreateView):
    model = Curso
    template_name = "curso/crearcurso.html"
    form_class = CursoForm
    success_url = reverse_lazy('curso')
    permission_required = 'core.add_curso'

class curso (PermissionRequiredMixin,ListView):
    model = Curso
    template_name = "curso/curso.html"
    permission_required = 'core.view_curso'


class modificarcurso(PermissionRequiredMixin,UpdateView):
    model = Curso
    template_name = "curso/modificarcurso.html"
    form_class = CursoForm
    success_url = reverse_lazy('curso')
    permission_required = 'core.change_curso'

class eliminarcurso(PermissionRequiredMixin,DeleteView):
    model = Curso
    template_name = "curso/verificar_curso.html"
    success_url = reverse_lazy('curso')
    permission_required = 'core.delete_curso'

class crearestudiante(PermissionRequiredMixin,CreateView):
    model = Estudiante
    template_name = "estudiante/crearestudiante.html"
    form_class = EstudianteForm
    success_url = reverse_lazy('estudiantes')
    permission_required = 'core.add_estudiante'

class estudiantes (PermissionRequiredMixin,ListView):
    model = Estudiante
    template_name = "estudiante/estudiantes.html"
    permission_required = 'core.view_estudiante'


class modificarestudiante(PermissionRequiredMixin,UpdateView):
    model = Estudiante
    template_name = "estudiante/modificarestudiante.html"
    form_class = EstudianteForm
    success_url = reverse_lazy('estudiantes')
    permission_required = 'core.change_estudiante'

class eliminarestudiante(PermissionRequiredMixin,DeleteView):
    model = Estudiante
    template_name = "estudiante/verifica_estudiante.html"
    success_url = reverse_lazy('estudiantes')
    permission_required = 'core.delete_estudiante'


class crearfamilia(PermissionRequiredMixin,CreateView):
    model = Familia
    template_name = "familia/crearfamilia.html"
    form_class = FamiliaForm
    success_url = reverse_lazy('familia')
    permission_required = 'core.add_familia'

class  familia (PermissionRequiredMixin,ListView):
    model = Familia
    template_name = "familia/familia.html"
    permission_required = 'core.view_familia'

class modificarfamilia(PermissionRequiredMixin,UpdateView):
    model = Familia
    template_name = "familia/modificarfamilia.html"
    form_class = FamiliaForm
    success_url = reverse_lazy('familia')
    permission_required = 'core.change_familia'

class eliminarfamilia(PermissionRequiredMixin,DeleteView):
    model = Familia
    template_name = "familia/verifica_familia.html"
    success_url = reverse_lazy('familia')
    permission_required = 'core.delete_familia'


class crearenfermedad(PermissionRequiredMixin,CreateView):
    model = Enfermedad
    template_name = "enfermedad/crearenfermedad.html"
    form_class = EnfermedadForm
    success_url = reverse_lazy('enfermedades')
    permission_required = 'core.add_enfermedad'

class modificarenfermedad(PermissionRequiredMixin,UpdateView):
    model = Enfermedad
    template_name = "enfermedad/modificarenfermedad.html"
    form_class = EnfermedadForm
    success_url = reverse_lazy('enfermedades')
    permission_required = 'core.change_enfermedad'


class enfermedades (PermissionRequiredMixin,ListView):
    model = Enfermedad
    template_name = "enfermedad/Enfermedades.html"
    permission_required = 'core.view_enfermedad'

class eliminarenfermedad(PermissionRequiredMixin,DeleteView):
    model = Enfermedad
    template_name = "enfermedad/verifica_enfermedad.html"
    success_url = reverse_lazy('enfermedades')
    permission_required = 'core.delete_enfermedad'


class crearretiro(PermissionRequiredMixin,CreateView):
    model = Retiro
    template_name = "retiro/crearretiro.html"
    form_class = RetiroForm
    success_url = reverse_lazy('retiro')
    permission_required = 'core.add_retiro'


class modificarretiro(PermissionRequiredMixin,UpdateView):
    model = Retiro
    template_name = "retiro/modificarretiro.html"
    form_class = RetiroForm
    success_url = reverse_lazy('retiro')
    permission_required = 'core.change_retiro'

class retiro (PermissionRequiredMixin,ListView):
    model = Retiro
    template_name = "retiro/Retiro.html"
    permission_required = 'core.view_retiro'

class eliminarretiro(PermissionRequiredMixin,DeleteView):
   model = Retiro
   template_name = "retiro/verifica_retiro.html"
   success_url = reverse_lazy('retiro')
   permission_required = 'core.delete_retiro'




def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
@login_required(None,"",'login')
def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/welcome')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})



