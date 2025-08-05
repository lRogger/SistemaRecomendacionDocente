# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('encuesta-profesor-FL/', views.obtener_resultados_FL_profesores, name='obtener_resultados_FL_profesores'),
]
