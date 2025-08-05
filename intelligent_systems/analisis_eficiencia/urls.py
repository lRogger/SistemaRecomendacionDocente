# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('resultados-encuesta-profesor/', views.obtener_resultados_encuesta_profesores, name='obtener_resultados_encuesta_profesores'),
    path('resultados-encuesta-estudiante/', views.obtener_resultados_encuesta_estudiantes, name='obtener_resultados_encuesta_estudiante'),
    path('resultados-asignacion-docentes/', views.obtener_resultados_asignacion_docentes, name='obtener_resultados_asignacion_docentes'),
    path('validacion-modelos/', views.validar_modelos, name='validar_modelos'),
    path('validacion-docentes/', views.obtener_resultados_compatibilidad_docentes, name='validacion_docentes'),
]