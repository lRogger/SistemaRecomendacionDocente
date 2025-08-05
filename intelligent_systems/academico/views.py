# views.py
from django.http import JsonResponse
from .models import Profesor

def buscar_profesores(request):
    query = request.GET.get('q', '')  # Obtiene el término de búsqueda desde el parámetro 'q'
    
    # Realiza la búsqueda en el modelo 'Profesor'
    profesores = Profesor.objects.filter(
        nombre__icontains=query  # Busca coincidencias parciales en el campo 'nombre'
    )[:10]  # Limita los resultados a los 10 primeros

    # Crea una lista de diccionarios con los datos relevantes
    data = [
        {"id": profesor.id, "nombre": f"{profesor.nombre}"}
        for profesor in profesores
    ]

    return JsonResponse(data, safe=False)  # Devuelve los datos como JSON
