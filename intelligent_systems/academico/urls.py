# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('buscar-profesores/', views.buscar_profesores, name='buscar_profesores'),
]
