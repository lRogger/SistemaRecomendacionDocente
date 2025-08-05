from django.db.models import Avg
from .models import EncuestaProfesor, EncuestaEstudiante, Asignatura, Profesor

def obtener_datos_encuestas(profesor_id=None):
    # Datos de profesores (Promedio por materia)
    encuestas_query = EncuestaProfesor.objects.values(
        'id', 'profesor__nombre', 
        'introduccion_pregunta_1',
        'introduccion_pregunta_2',
        'introduccion_pregunta_3',
        'proceso_software_pregunta_1',
        'proceso_software_pregunta_2',
        'proceso_software_pregunta_3',
        'ing_requerimientos_pregunta_1',
        'ing_requerimientos_pregunta_2',
        'ing_requerimientos_pregunta_3',
        'model_software_pregunta_1',
        'model_software_pregunta_2',
        'model_software_pregunta_3',
        'dise_arqui_software_pregunta_1',
        'dise_arqui_software_pregunta_2',
        'dise_arqui_software_pregunta_3',
        'hombre_maquina_pregunta_1',
        'hombre_maquina_pregunta_2',
        'hombre_maquina_pregunta_3',
        'construccion_software_pregunta_1',
        'construccion_software_pregunta_2',
        'construccion_software_pregunta_3',
        'experiencia_usuario_pregunta_1',
        'experiencia_usuario_pregunta_2',
        'experiencia_usuario_pregunta_3',
        'calidad_software_pregunta_1',
        'calidad_software_pregunta_2',
        'calidad_software_pregunta_3',
        'validacion_software_pregunta_1',
        'validacion_software_pregunta_2',
        'validacion_software_pregunta_3',
        'configuracion_software_pregunta_1',
        'configuracion_software_pregunta_2',
        'configuracion_software_pregunta_3',
        'auditoria_software_pregunta_1',
        'auditoria_software_pregunta_2',
        'auditoria_software_pregunta_3',
        # Agregar otras materias según corresponda
    )
    if profesor_id is not None:
        encuestas_query = encuestas_query.filter(profesor_id=profesor_id)
    
    # Datos de estudiantes (Promedio de experiencia por materia y profesor)
    # datos_estudiantes = EncuestaEstudiante.objects.values('asignatura', 'profesor').annotate(
    #     promedio_experiencia=Avg('pregunta_1')  # Ajusta esto para incluir más preguntas
    # )

# , list(datos_estudiantes)
    return list(encuestas_query)

def obtener_datos_encuestas_estudiantes(profesor_id=None):
    encuestras_query = EncuestaEstudiante.objects.select_related('profesor', 'asignatura').values(
        'id',
        'estudiante',
        'asignatura__nombre',  # Ejemplo de obtener un campo específico
        'profesor__nombre', 
        'profesor__id', 
        'pregunta_1',
        'pregunta_2',
        'pregunta_3',
        'pregunta_4',
        'pregunta_5',
        'pregunta_6',
        'pregunta_7',
        'pregunta_8',
        'pregunta_9',
        'pregunta_10',
        'pregunta_11',
    )
    if profesor_id is not None:
        encuestras_query = encuestras_query.filter(profesor_id=profesor_id)

    return list(encuestras_query)


def arreglo_materias():
    return {
        'Introducción a Ingeniería de Software': [
            'introduccion_pregunta_1', 'introduccion_pregunta_2', 'introduccion_pregunta_3'
        ],
        'Proceso de Software': [
            'proceso_software_pregunta_1', 'proceso_software_pregunta_2', 'proceso_software_pregunta_3'
        ],
        'Ingeniería de Requerimiento': [
            'ing_requerimientos_pregunta_1', 'ing_requerimientos_pregunta_2', 'ing_requerimientos_pregunta_3'
        ],
        'Modelamiento de Software': [
            'model_software_pregunta_1', 'model_software_pregunta_2', 'model_software_pregunta_3',
        ],
        'Diseño y arquitectura de Software': [
            'dise_arqui_software_pregunta_1', 'dise_arqui_software_pregunta_2', 'dise_arqui_software_pregunta_3',
        ],
        'Interacción Hombre - Máquina': [
            'hombre_maquina_pregunta_1', 'hombre_maquina_pregunta_2', 'hombre_maquina_pregunta_3',
        ],
        'Construcción de Software': [
            'construccion_software_pregunta_1', 'construccion_software_pregunta_2', 'construccion_software_pregunta_3',
        ],
        'Diseño y experiencia de Usuario': [
            'experiencia_usuario_pregunta_1', 'experiencia_usuario_pregunta_2', 'experiencia_usuario_pregunta_3',
        ],
        'Calidad de Software': [
            'calidad_software_pregunta_1', 'calidad_software_pregunta_2', 'calidad_software_pregunta_3',
        ],
        'Verificación y Validación de Software': [
            'validacion_software_pregunta_1', 'validacion_software_pregunta_2', 'validacion_software_pregunta_3',
        ],
        'Gestión de la Configuración del Software': [
            'configuracion_software_pregunta_1', 'configuracion_software_pregunta_2', 'configuracion_software_pregunta_3',
        ],
        'Auditoria de Software': [
            'auditoria_software_pregunta_1', 'auditoria_software_pregunta_2', 'auditoria_software_pregunta_3',
        ],
    }


def listado_materias():
    return list(Asignatura.objects.values_list('nombre', flat=True))

def listado_docentes():
    return list(Profesor.objects.values_list('nombre', flat=True))
