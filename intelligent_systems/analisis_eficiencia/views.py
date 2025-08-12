from django.shortcuts import render
from academico import utils as utils_academico
from django.http import JsonResponse
from django.contrib import messages
from AST.utils import arbol_sintaxis_profesores, arbol_sintaxis_estudiantes
from FL.utils import logica_difusa_profesores, logica_difusa_estudiantes
from django.http import JsonResponse
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

from sklearn.metrics import confusion_matrix, recall_score
import numpy as np
# from intelligent_systems.academico import urls as utils_academico
from NEUTRO.utils import analisis_neutrosofico_profesores, analisis_neutrosofico_estudiantes

# Create your views here.
def analisis_Eficiencia_View(request):
    return render(request, 'analisis_comparativo.html', {})

def  lista_docentes_asignados_View(request):
    return render(request, 'docentes_asignados.html', {})

def analisis_docente_View(request):
    return render(request, 'analisis_docente.html', {})

def obtener_resultados_encuesta_estudiantes(request):
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
    datos_estudiantes = utils_academico.obtener_datos_encuestas_estudiantes(profesor_id=profesor_id)


    # Procesar datos
    resultadosAST = arbol_sintaxis_estudiantes(datos_estudiantes)
    resultadosFL = logica_difusa_estudiantes(datos_estudiantes)

    top_ast = sorted(resultadosAST, key=lambda x: x['probabilidad'], reverse=True)[:3]
    top_fl = sorted(resultadosFL, key=lambda x: x['probabilidad'], reverse=True)[:3]

    for item in top_ast:
        item['algoritmo'] = 'Árbol de Sintaxis Abstracta'
    for item in top_fl:
        item['algoritmo'] = 'Lógica Neutrosófica'


    return JsonResponse({
        'ast_values': resultadosAST,
        'fl_values': resultadosFL,
        'comparation_values': top_ast + top_fl
    }, safe=False)

def obtener_resultados_encuesta_profesores(request):
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


    # Procesar datos
    resultadosAST = arbol_sintaxis_profesores(datos_profesores)
    resultadosFL = logica_difusa_profesores(datos_profesores)

    top_ast = sorted(resultadosAST, key=lambda x: x['probabilidad'], reverse=True)[:3]
    top_fl = sorted(resultadosFL, key=lambda x: x['probabilidad'], reverse=True)[:3]

    for item in top_ast:
        item['algoritmo'] = 'Árbol de Sintaxis Abstracta'
    for item in top_fl:
        item['algoritmo'] = 'Lógica Neutrosófica'


    return JsonResponse({
        'ast_values': resultadosAST,
        'fl_values': resultadosFL,
        'comparation_values': top_ast + top_fl
    }, safe=False)


def obtener_resultados_asignacion_docentes(request):
    try:
        datos_profesores = utils_academico.obtener_datos_encuestas()
        datos_estudiantes = utils_academico.obtener_datos_encuestas_estudiantes()
        ast_estudiantes = arbol_sintaxis_estudiantes(datos_estudiantes)
        fl_estudiantes = logica_difusa_estudiantes(datos_estudiantes)
        ast_profesores = arbol_sintaxis_profesores(datos_profesores)
        fl_profesores = logica_difusa_profesores(datos_profesores)
        resultados = asignacion_docentes(ast_profesores, fl_profesores, ast_estudiantes, fl_estudiantes)
        return JsonResponse(resultados, safe=False)
    except Exception as e:
        messages.error(request, str(e))
        return JsonResponse({'error': str(e)}, status=500)

    


def asignacion_docentes(ast_profesores, fl_profesores, ast_estudiantes, fl_estudiantes, neutro_profesores=None, neutro_estudiantes=None):
    # Si no se pasan los resultados neutrosóficos, calcularlos aquí (para compatibilidad)
    if neutro_profesores is None or neutro_estudiantes is None:
        datos_profesores = utils_academico.obtener_datos_encuestas()
        datos_estudiantes = utils_academico.obtener_datos_encuestas_estudiantes()
        neutro_profesores = analisis_neutrosofico_profesores(datos_profesores)
        neutro_estudiantes = analisis_neutrosofico_estudiantes(datos_estudiantes)

    # Crear índices para acceso rápido
    index_neutro_prof = {(item['profesor'], item['materia']): item for item in neutro_profesores}
    index_neutro_est = {(item['profesor'], item['materia']): item for item in neutro_estudiantes}

    combinados = []

    def buscar_puntaje(lista, profesor, materia):
        promedio_probabilidad = []
        for item in lista:
            if item['profesor'] == profesor and item['materia'] == materia:
                promedio_probabilidad.append(item['probabilidad'])
        if not promedio_probabilidad:
            return 0
        return sum(promedio_probabilidad) / len(promedio_probabilidad)
    
    lista_materias = utils_academico.listado_materias()
    lista_profesores = utils_academico.listado_docentes()

    for materia in lista_materias:
        for profesor in lista_profesores:
            puntaje_ast_prof = buscar_puntaje(ast_profesores, profesor, materia)
            puntaje_fl_prof = buscar_puntaje(fl_profesores, profesor, materia)
            puntaje_ast_est = buscar_puntaje(ast_estudiantes, profesor, materia)
            puntaje_fl_est = buscar_puntaje(fl_estudiantes, profesor, materia)

            promedio_ast = (puntaje_ast_prof + puntaje_ast_est) / 2
            promedio_fl = (puntaje_fl_prof + puntaje_fl_est) / 2
            puntaje_promedio = (0.5 * promedio_ast + 0.5 * promedio_fl)
            puntaje_promedio_ponderado = (0.4 * puntaje_ast_prof + 0.3 * puntaje_fl_prof + 0.2 * puntaje_ast_est + 0.1 * puntaje_fl_est)

            # Buscar valores neutrosóficos
            neutro_prof = index_neutro_prof.get((profesor, materia), {})
            neutro_est = index_neutro_est.get((profesor, materia), {})

            combinados.append({
                'profesor': profesor,
                'materia': materia,
                'puntaje_promedio': round(puntaje_promedio, 2),
                'puntaje_ast_prof': round(puntaje_ast_prof, 2),
                'puntaje_ast_est': round(puntaje_ast_est, 2),
                'promedio_ast': round(promedio_ast, 2),
                'promedio_fl': round(promedio_fl, 2),
                'puntaje_fl_prof': round(puntaje_fl_prof, 2),
                'puntaje_fl_est': round(puntaje_fl_est, 2),
                # Neutrosofía profesor
                'T_neutro_prof': neutro_prof.get('T') if neutro_prof.get('T') else 0,
                'I_neutro_prof': neutro_prof.get('I') if neutro_prof.get('I') else 0,
                'F_neutro_prof': neutro_prof.get('F') if neutro_prof.get('F') else 0,
                'score_neutro_prof': neutro_prof.get('score') if neutro_prof.get('score') else 0,
                'deneutrosophy_prof': neutro_prof.get('deneutrosophy') if neutro_prof.get('deneutrosophy') else 0,
                # Neutrosofía estudiante

                'T_neutro_est': neutro_est.get('T') if neutro_est.get('T') else 0,
                'I_neutro_est': neutro_est.get('I') if neutro_est.get('I') else 0,
                'F_neutro_est': neutro_est.get('F') if neutro_est.get('F') else 0,
                'score_neutro_est': neutro_est.get('score') if neutro_est.get('score') else 0,
                'deneutrosophy_est': neutro_est.get('deneutrosophy') if neutro_est.get('deneutrosophy') else 0,
            })

    combinados = sorted(combinados, key=lambda x: x['puntaje_promedio'], reverse=True)

    materias_asignadas = set()
    profesores_asignados = set()
    asignaciones = []

    for materia in lista_materias:
        objetos_filtrados = [obj for obj in combinados if obj["materia"] == materia]
        for objeto in objetos_filtrados:
            if objeto["profesor"] in [asignacion["profesor"] for asignacion in asignaciones]:
                continue
            asignaciones.append({
                "profesor": objeto["profesor"],
                "materia": objeto["materia"],
                "puntaje_promedio": objeto["puntaje_promedio"],
                "puntaje_ast_prof": objeto["puntaje_ast_prof"],
                "puntaje_ast_est": objeto["puntaje_ast_est"],
                "promedio_ast": objeto["promedio_ast"],
                "promedio_fl": objeto["promedio_fl"],
                "puntaje_fl_prof": objeto["puntaje_fl_prof"],
                "puntaje_fl_est": objeto["puntaje_fl_est"],
                # Neutrosofía profesor
                'T_neutro_prof': objeto.get('T_neutro_prof'),
                'I_neutro_prof': objeto.get('I_neutro_prof'),
                'F_neutro_prof': objeto.get('F_neutro_prof'),
                'score_neutro_prof': objeto.get('score_neutro_prof'),
                'deneutrosophy_prof': objeto.get('deneutrosophy_prof'),
                # Neutrosofía estudiante
                'T_neutro_est': objeto.get('T_neutro_est'),
                'I_neutro_est': objeto.get('I_neutro_est'),
                'F_neutro_est': objeto.get('F_neutro_est'),
                'score_neutro_est': objeto.get('score_neutro_est'),
                'deneutrosophy_est': objeto.get('deneutrosophy_est'),
            })
            break
    asignaciones = sorted(asignaciones, key=lambda x: x['puntaje_promedio'], reverse=True)
    return asignaciones




def validar_modelos(request):
    try:
        profesor_id = request.GET.get('id')

        if profesor_id is None:
            return JsonResponse({'error': 'El parámetro id es obligatorio.'}, status=400)

        try:
            # Convertir a entero si es necesario
            profesor_id = int(profesor_id)
        except ValueError:
            return JsonResponse({'error': 'El parámetro id debe ser un número válido.'}, status=400)

        # Obtener los datos del profesor específico
        
        # Datos obtenidos del análisis AST y FL
        datos_profesores = utils_academico.obtener_datos_encuestas(profesor_id=profesor_id)
        datos_estudiantes = utils_academico.obtener_datos_encuestas_estudiantes(profesor_id=profesor_id)
        # 'comparation_values': top_ast + top_fl
        ast_estudiantes = arbol_sintaxis_estudiantes(datos_estudiantes)
        fl_estudiantes = logica_difusa_estudiantes(datos_estudiantes)
        ast_profesores = arbol_sintaxis_profesores(datos_profesores)
        fl_profesores = logica_difusa_profesores(datos_profesores)

        
        # Agrupación por profesor y materia
        resultados_agrupados = {
            'AST': calcular_matriz_confusion(ast_estudiantes + ast_profesores ),
            'FL': calcular_matriz_confusion(fl_estudiantes + fl_profesores),
        }



        

        return JsonResponse(resultados_agrupados)
    except Exception as e:
        messages.error(request, str(e))


def calcular_matriz_confusion(data, umbral=50):
    """
    Calcula la matriz de confusión y el recall basado en un umbral.
    
    :param data: Diccionario con las claves 'ast_values' y 'fl_values'.
    :param umbral: Umbral de probabilidad para considerar una predicción como válida.
    :return: Diccionario con las métricas de evaluación para AST y FL.
    """

    def procesar_datos(values):
        """
        Genera las etiquetas reales y predichas |en base al umbral.
        
        :param values: Lista de resultados del algoritmo (AST o FL).
        :return: Etiquetas reales y predichas.
        """
        y_true = []  # Simulación de etiquetas reales (siempre 1).
        y_pred = []  # Predicciones basadas en el umbral.

        for item in values:
            y_true.append(1)  # Se asume que siempre es un caso real.
            y_pred.append(1 if item['probabilidad'] >= umbral else 0)

        return y_true, y_pred

    # Procesar AST
    y_true, y_pred = procesar_datos(data)
    matriz = confusion_matrix(y_true, y_pred, labels=[1, 0])
    recall = recall_score(y_true, y_pred, pos_label=1)

    return {
        "matriz_confusion": matriz.tolist(),
        "recall": round(recall, 2),
        "total_correcto": sum(y_true),
        "total_predicciones": len(y_pred)
    }

def obtener_resultados_compatibilidad_docentes(request):
    try:
        profesor_id = request.GET.get('id')

        if profesor_id is None:
            return JsonResponse({'error': 'El parámetro id es obligatorio.'}, status=400)
        # Convertir a entero si es necesario
        profesor_id = int(profesor_id)
        datos_profesores = utils_academico.obtener_datos_encuestas(profesor_id)
        datos_estudiantes = utils_academico.obtener_datos_encuestas_estudiantes(profesor_id)
        ast_estudiantes = arbol_sintaxis_estudiantes(datos_estudiantes)
        fl_estudiantes = logica_difusa_estudiantes(datos_estudiantes)
        ast_profesores = arbol_sintaxis_profesores(datos_profesores)
        fl_profesores = logica_difusa_profesores(datos_profesores)
        resultados = compatibilidad_docente(ast_profesores, fl_profesores, ast_estudiantes, fl_estudiantes)
        return JsonResponse(resultados, safe=False)
    except Exception as e:
        messages.error(request, str(e))


def compatibilidad_docente(ast_profesores, fl_profesores, ast_estudiantes, fl_estudiantes):
    

    # Combinar los resultados de AST y FL por materia y profesor
    combinados = []

    def buscar_puntaje(lista, materia):
        # Busca el puntaje en la lista dada por profesor y materia
        promedio_probabilidad = []
        for item in lista:
            if item['materia'] == materia:
                promedio_probabilidad.append(item['probabilidad'])

        if not promedio_probabilidad:
            return 0  # Retornar un valor predeterminado
        return sum(promedio_probabilidad) / len(promedio_probabilidad)  # Retorna 0 si no encuentra coincidencia
    
    lista_materias = utils_academico.listado_materias()

    for materia in lista_materias:
        puntaje_ast_prof = buscar_puntaje(ast_profesores, materia)
        puntaje_fl_prof = buscar_puntaje(fl_profesores, materia)
        puntaje_ast_est = buscar_puntaje(ast_estudiantes, materia)
        puntaje_fl_est = buscar_puntaje(fl_estudiantes, materia)



    # Calcular promedios por algoritmo
        promedio_ast = (puntaje_ast_prof + puntaje_ast_est) / 2
        promedio_fl = (puntaje_fl_prof + puntaje_fl_est) / 2

        # Calcular el puntaje promedio general ponderado
        puntaje_promedio = (0.5 * promedio_ast + 0.5 * promedio_fl)

        puntaje_promedio_ponderado = (0.4 * puntaje_ast_prof + 0.3 * puntaje_fl_prof +
                            0.2 * puntaje_ast_est + 0.1 * puntaje_fl_est)

        combinados.append({
            'materia': materia,
            'puntaje_promedio': round(puntaje_promedio, 2),
            'puntaje_ast_prof': round(puntaje_ast_prof, 2),
            'puntaje_ast_est': round(puntaje_ast_est, 2),
            'promedio_ast': round(promedio_ast, 2),
            'promedio_fl': round(promedio_fl, 2),
            'puntaje_fl_prof': round(puntaje_fl_prof, 2),
            'puntaje_fl_est': round(puntaje_fl_est, 2),
        })

    # Ordenar los combinados por puntaje promedio de mayor a menor
    combinados = sorted(combinados, key=lambda x: x['puntaje_promedio'], reverse=True)

    # Asignar docentes a materias
    materias_asignadas = set()
    profesores_asignados = set()
    asignaciones = []

    for materia in lista_materias:
        objetos_filtrados = [obj for obj in combinados if obj["materia"] == materia]

        for objeto in objetos_filtrados:
            # Asignar el profesor a la materia
            asignaciones.append({
                "materia": objeto["materia"],
                "puntaje_promedio": objeto["puntaje_promedio"],
                "puntaje_ast_prof": objeto["puntaje_ast_prof"],
                "puntaje_ast_est": objeto["puntaje_ast_est"],
                "promedio_ast": objeto["promedio_ast"],
                "promedio_fl": objeto["promedio_fl"],
                "puntaje_fl_prof": objeto["puntaje_fl_prof"],
                "puntaje_fl_est": objeto["puntaje_fl_est"],
            })
            break  # Detener el ciclo cuando se haya asignado la materia a un profesor disponible
    
    asignaciones = sorted(asignaciones, key=lambda x: x['puntaje_promedio'], reverse=True)

    return asignaciones