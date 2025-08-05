# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('encuesta-profesor-AST/', views.obtener_resultados_AST_profesores, name='obtener_resultados_AST_profesores'),
]