from django.urls import path
from . import views

urlpatterns = [
    path('profesores/', views.resultados_neutro_profesores, name='resultados_neutro_profesores'),
    path('estudiantes/', views.resultados_neutro_estudiantes, name='resultados_neutro_estudiantes'),
] 