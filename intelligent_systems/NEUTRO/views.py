# views.py para el módulo neutro

from django.http import JsonResponse
from django.shortcuts import render
from academico import utils as utils_academico
from .utils import analisis_neutrosofico_profesores, analisis_neutrosofico_estudiantes

def neutro_analisis_view(request):
    """Vista principal para el análisis neutrosófico"""
    return render(request, 'analisis_neutro.html')

def resultados_neutro_profesores(request):
    profesor_id = request.GET.get('id')
    if profesor_id is None:
        return JsonResponse({'error': 'El parámetro id es obligatorio.'}, status=400)
    try:
        profesor_id = int(profesor_id)
    except ValueError:
        return JsonResponse({'error': 'El parámetro id debe ser un número válido.'}, status=400)
    datos_profesores = utils_academico.obtener_datos_encuestas(profesor_id=profesor_id)
    resultados = analisis_neutrosofico_profesores(datos_profesores)
    return JsonResponse(resultados, safe=False)

def resultados_neutro_estudiantes(request):
    datos_estudiantes = utils_academico.obtener_datos_encuestas_estudiantes()
    resultados = analisis_neutrosofico_estudiantes(datos_estudiantes)
    return JsonResponse(resultados, safe=False) 