
# import pandas as pd
from django.shortcuts import render
import html
from .forms import CargarExcelForm
from .utils import cargar_encuesta_profesores_desde_excel, cargar_encuesta_estudiantes_desde_excel
from django.contrib import messages
from django.db import transaction
from academico.models import Asignatura, Profesor ,Estudiante ,EncuestaEstudiante, EncuestaProfesor
from django.http import JsonResponse


def migration_Excel_View(request):
    if request.method == 'POST':
        
        archivo_excel_estudiantes = request.FILES['archivo_excel_estudiantes']
        archivo_excel_profesores = request.FILES['archivo_excel_profesores']

        if not archivo_excel_estudiantes or not archivo_excel_profesores:
            messages.error(request, f"Por favor, cargue ambos archivos")
        else:
            try:
                with transaction.atomic():  # Bloque de transacción
                    if archivo_excel_profesores:
                        cargar_encuesta_profesores_desde_excel(archivo_excel_profesores)
                    if archivo_excel_estudiantes:
                        cargar_encuesta_estudiantes_desde_excel(archivo_excel_estudiantes)
                    messages.success(request, f"Subida de archivos correctamente")
            except Exception as e:
                mensaje_error = html.unescape(str(e))
                messages.error(request, f"{mensaje_error}")

    return render(request, 'migration_excel.html', {'form': CargarExcelForm()})


def limpiar_tablas(request):
    if request.method == 'POST':  # Aseguramos que es un método POST
        try:
            # Eliminar todos los registros de las tablas
            Profesor.objects.all().delete()
            Estudiante.objects.all().delete()
            EncuestaEstudiante.objects.all().delete()
            EncuestaProfesor.objects.all().delete()
            Asignatura.objects.all().delete()

            # Respuesta de éxito
            return JsonResponse({'message': 'Tablas limpiadas con éxito'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)