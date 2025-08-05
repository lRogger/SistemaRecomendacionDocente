# urls.py
from django.urls import path, include

urlpatterns = [
    path('academico/', include('academico.urls')),
    path('analisis-eficiencia/', include('analisis_eficiencia.urls')),
    path('migration-excel/', include('migration_excel.urls'))
]
