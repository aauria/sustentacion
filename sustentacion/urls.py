"""sustentacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from core import views

urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('portada/', views.portada, name="portada"),
    url('usuario/',include('usuario.urls')),
    path('', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('MyV/', views.MyV, name="MyV"),
    path('curso/', views.curso.as_view(), name="curso"),
    path('modificarcurso/<int:pk>', views.modificarcurso.as_view(), name="modificarcurso"),
    path('crearcurso/', views.crearcurso.as_view(), name='crearcurso'),
    path('eliminarcurso/<int:pk>', views.eliminarcurso.as_view(), name="eliminarcurso"),
    path('estudiantes/', views.estudiantes.as_view(), name="estudiantes"),
    path('modificarestudiante/<int:pk>', views.modificarestudiante.as_view(), name="modificarestudiante"),
    path('crearestudiante/', views.crearestudiante.as_view(), name="crearestudiante"),
    path('eliminarestudiante/<int:pk>', views.eliminarestudiante.as_view(), name="eliminarestudiante"),
    path('familia/', views.familia.as_view(), name="familia"),
    path('modificarfamilia/<int:pk>', views.modificarfamilia.as_view(), name="modificarfamilia"),
    path('crearfamilia/', views.crearfamilia.as_view(), name="crearfamilia"),
    path('eliminarfamilia/<int:pk>', views.eliminarfamilia.as_view(), name="eliminarfamilia"),
    path('enfermedades/', views.enfermedades.as_view(), name="enfermedades"),
    path('modificarenfermedad/<int:pk>', views.modificarenfermedad.as_view(), name="modificarenfermedad"),
    path('crearenfermedad/', views.crearenfermedad.as_view(), name="crearenfermedad"),
    path('eliminarenfermedad/<int:pk>', views.eliminarenfermedad.as_view(), name="eliminarenfermedad"),
    path('retiro/', views.retiro.as_view(), name='retiro'),
    path('modificarretiro/<int:pk>', views.modificarretiro.as_view(), name="modificarretiro"),
    path('crearretiro/', views.crearretiro.as_view(), name="crearretiro"),
    path('eliminarretiro/<int:pk>', views.eliminarretiro.as_view(), name="eliminarretiro"),
    path('admin/', admin.site.urls),
]