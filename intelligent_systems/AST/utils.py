from anytree import Node, RenderTree
from academico import utils as utils_academico
from anytree.exporter import DictExporter


exporter = DictExporter() 


def arbol_sintaxis_profesores(datos_profesores):
    # Estructura de materias con sus preguntas
    materias_preguntas = utils_academico.arreglo_materias()

    resultados = []
    for datos in datos_profesores:
        # Crear el nodo raíz del árbol para cada profesor
        raiz = Node(f"Evaluación del Profesor: {datos['profesor__nombre']}")

        for materia, preguntas in materias_preguntas.items():
            nodo_materia = Node(materia, parent=raiz)
            valores_preguntas = []

            for pregunta in preguntas:
                if pregunta in datos:  # Verificar si la pregunta está en los datos
                    valor_pregunta = datos[pregunta]
                    valores_preguntas.append(valor_pregunta)
                    Node(f"{pregunta}: {valor_pregunta}", parent=nodo_materia, value=valor_pregunta)

            # Calcular el puntaje promedio para la materia
            if valores_preguntas:
                puntaje_materia = sum(valores_preguntas) / len(valores_preguntas)
            else:
                puntaje_materia = 0  # Si no hay preguntas, el puntaje es 0

            # Guardar el resultado por materia
            resultados.append({
                'profesor': datos['profesor__nombre'],
                'materia': materia,
                'puntaje': puntaje_materia,
                'probabilidad': round((puntaje_materia / 5) * 100, 2),
                # 'estructura_arbol': exporter.export(raiz)  # Representación del árbol
            })

    return resultados


def arbol_sintaxis_estudiantes(encuestas):
    resultados = []
    
    # Agrupar encuestas por profesor y asignatura
    datos_agrupados = {}
    for encuesta in encuestas:
        profesor = encuesta['profesor__nombre']
        materia = encuesta['asignatura__nombre']
        clave = (profesor, materia)

        if clave not in datos_agrupados:
            datos_agrupados[clave] = []

        # Agregar las respuestas de las preguntas al grupo correspondiente
        datos_agrupados[clave].append([
            encuesta['pregunta_1'], encuesta['pregunta_2'], encuesta['pregunta_3'], encuesta['pregunta_4'],
            encuesta['pregunta_5'], encuesta['pregunta_6'], encuesta['pregunta_7'], encuesta['pregunta_8'],
            encuesta['pregunta_9'], encuesta['pregunta_10'], encuesta['pregunta_11']
        ])

    # Procesar cada grupo de encuestas
    for (profesor, materia), respuestas in datos_agrupados.items():
        # Crear el árbol para la materia y calcular puntajes
        raiz = Node(f"Evaluación de {materia} - {profesor}")
        promedio_preguntas = []

        for idx, pregunta in enumerate(zip(*respuestas), start=1):  # Transponer para agrupar preguntas
            promedio = sum(pregunta) / len(pregunta)
            promedio_preguntas.append(promedio)
            Node(f"Pregunta {idx}: {round(promedio, 2)}", parent=raiz, value=promedio)

        # Puntaje final como el promedio de todas las preguntas
        puntaje_final = sum(promedio_preguntas) / len(promedio_preguntas)
        
        
        resultados.append({
            'profesor': profesor,
            'materia': materia,
            'puntaje': round(puntaje_final, 2),  # Puntaje promedio final
            'probabilidad': round((puntaje_final / 5) * 100, 2),  # Puntaje promedio final
            # 'estructura_arbol': exporter.export(raiz)  # Representación del árbol
        })

    return resultados
