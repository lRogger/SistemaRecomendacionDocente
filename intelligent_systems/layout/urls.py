from django.urls import path, include

from . import views
from migration_excel import views as migration_excel_views
from analisis_eficiencia import views as analisis_eficiencia_views
from NEUTRO import views as neutro_views

urlpatterns=[
    path('', views.homeLayout, name='index'),
    path('migration/', migration_excel_views.migration_Excel_View, name='migration_excel'),
    path('analisis-eficiencia/', analisis_eficiencia_views.analisis_Eficiencia_View, name='analisis_eficiencia'),
    path('docentes-asignados/', analisis_eficiencia_views.lista_docentes_asignados_View, name='docentes_asignados'),
    path('analisis-docente/', analisis_eficiencia_views.analisis_docente_View, name='analisis_docente'),
    path('neutro/', neutro_views.neutro_analisis_view, name='neutro_analisis'),
]