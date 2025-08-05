from django.urls import path, include

from . import views

urlpatterns=[
    path('limpieza-tablas/', views.limpiar_tablas , name='limpiar_tablas'),
]