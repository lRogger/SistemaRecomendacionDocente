import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from academico import utils as utils_academico
from django.http import JsonResponse

def logica_difusa_profesores(datos_profesores):
    # Variables difusas
    conocimiento = ctrl.Antecedent(np.arange(1, 6, 1), 'conocimiento')
    experiencia = ctrl.Antecedent(np.arange(1, 6, 1), 'experiencia')
    probabilidad = ctrl.Consequent(np.arange(1, 6, 1), 'probabilidad')

    # Membership functions
    conocimiento.automf(3)  # Bajo, medio, alto
    experiencia.automf(3)
    probabilidad['baja'] = fuzz.trimf(probabilidad.universe, [1, 1, 3])
    probabilidad['media'] = fuzz.trimf(probabilidad.universe, [2, 3, 4])
    probabilidad['alta'] = fuzz.trimf(probabilidad.universe, [3, 5, 5])

    # Reglas
    rule1 = ctrl.Rule(conocimiento['poor'] & experiencia['poor'], probabilidad['baja'])
    rule2 = ctrl.Rule(conocimiento['average'] & experiencia['average'], probabilidad['media'])
    rule3 = ctrl.Rule(conocimiento['good'] & experiencia['good'], probabilidad['alta'])

    # Controlador
    control = ctrl.ControlSystem([rule1, rule2, rule3])
    simulador = ctrl.ControlSystemSimulation(control)

    resultados = []

    # Define las materias y sus preguntas asociadas
    materias = utils_academico.arreglo_materias()

    
    for datos in datos_profesores:
        for materia, preguntas in materias.items():
            # Obtén las respuestas asociadas a la materia
            respuestas = [datos[p] for p in preguntas]

            # Calcula el promedio de las respuestas
            promedio_respuestas = np.mean(respuestas)

            # Simulación para esta materia
            simulador.input['conocimiento'] = promedio_respuestas
            simulador.input['experiencia'] = promedio_respuestas  # Puedes ajustar esto si experiencia tiene otra lógica

            simulador.compute()

            resultados.append({
                'profesor': datos['profesor__nombre'],
                'materia': materia,
                'probabilidad': round(((simulador.output['probabilidad'] - 1) / 4) * 100, 2),
                'puntaje': float(simulador.output['probabilidad']),
            })

    return resultados


def obtener_resultados(request):
    # Recuperar el id desde los query parameters
    profesor_id = request.GET.get('id')

    if profesor_id is None:
        return JsonResponse({'error': 'El parámetro id es obligatorio.'}, status=400)

    try:
        # Convertir a entero si es necesario
        profesor_id = int(profesor_id)
    except ValueError:
        return JsonResponse({'error': 'El parámetro id debe ser un número válido.'}, status=400)

    # Obtener los datos del profesor específico
    datos_profesores = utils_academico.obtener_datos_encuestas(profesor_id=profesor_id)

    # Procesar con la lógica difusa
    resultados = logica_difusa_profesores(datos_profesores)

    return JsonResponse(resultados, safe=False)


def logica_difusa_estudiantes(encuestas):
    # Variables difusas
    experiencia = ctrl.Antecedent(np.arange(1, 6, 1), 'experiencia')
    satisfaccion = ctrl.Consequent(np.arange(1, 6, 1), 'satisfaccion')

    # Membership functions
    experiencia.automf(3)  # Bajo, medio, alto
    satisfaccion['baja'] = fuzz.trimf(satisfaccion.universe, [1, 1, 3])
    satisfaccion['media'] = fuzz.trimf(satisfaccion.universe, [2, 3, 4])
    satisfaccion['alta'] = fuzz.trimf(satisfaccion.universe, [3, 5, 5])

    # Reglas
    rule1 = ctrl.Rule(experiencia['poor'], satisfaccion['baja'])
    rule2 = ctrl.Rule(experiencia['average'], satisfaccion['media'])
    rule3 = ctrl.Rule(experiencia['good'], satisfaccion['alta'])

    # Sistema difuso
    control = ctrl.ControlSystem([rule1, rule2, rule3])
    simulador = ctrl.ControlSystemSimulation(control)

    # Agrupar encuestas por profesor y asignatura
    resultados = {}
    for encuesta in encuestas:
        profesor = encuesta['profesor__nombre']  # Acceso al nombre del profesor
        materia = encuesta['asignatura__nombre']  # Acceso al nombre de la asignatura
        clave = (profesor, materia)
        
        # Inicializar lista de experiencias si no existe
        if clave not in resultados:
            resultados[clave] = []

        # Promedio de las respuestas de las preguntas (1-11)
        preguntas = [
            encuesta['pregunta_1'], encuesta['pregunta_2'], encuesta['pregunta_3'], encuesta['pregunta_4'],
            encuesta['pregunta_5'], encuesta['pregunta_6'], encuesta['pregunta_7'], encuesta['pregunta_8'],
            encuesta['pregunta_9'], encuesta['pregunta_10'], encuesta['pregunta_11']
        ]
        resultados[clave].append(np.mean(preguntas))

    # Procesar resultados
    calificaciones = []
    for (profesor, materia), experiencias in resultados.items():
        promedio_experiencia = np.mean(experiencias)

        # Simulación de lógica difusa
        simulador.input['experiencia'] = promedio_experiencia
        simulador.compute()
        satisfaccion_final = simulador.output['satisfaccion']

        # Convertir la calificación en porcentaje
        satisfaccion_porcentaje = round((satisfaccion_final / 5) * 100, 2)

        # Guardar resultados
        calificaciones.append({
            'profesor': profesor,
            'materia': materia,
            'calificacion': round(satisfaccion_final, 2),
            'probabilidad': satisfaccion_porcentaje
        })

    return calificaciones