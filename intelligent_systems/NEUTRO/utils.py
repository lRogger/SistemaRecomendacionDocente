# utils.py para el módulo neutro

import math
from academico import utils as utils_academico

class SingleValuedNeutrosophicNumber:
    """Implementación propia de Single Valued Neutrosophic Number"""
    
    def __init__(self, id, truth, indeterminacy, falsehood):
        """Inicializar número neutrosófico con T, I, F"""
        assert 0 <= truth <= 1, 'invalid truth value'
        assert 0 <= indeterminacy <= 1, 'invalid indeterminacy value'
        assert 0 <= falsehood <= 1, 'invalid falsehood value'
        assert 0 <= truth + falsehood + indeterminacy <= 3, 'invalid combined sum values'
        
        self.id = id
        self.truth = truth
        self.indeterminacy = indeterminacy
        self.falsehood = falsehood
    
    def score(self):
        """Calcular score neutrosófico"""
        return (2 + self.truth - self.indeterminacy - self.falsehood) / 3
    
    def deneutrosophy(self):
        """Calcular deneutrosoficación"""
        return 1 - math.sqrt(((1 - self.truth)**2 + self.indeterminacy**2 + self.falsehood**2) / 3)
    
    def accuracy(self):
        """Calcular precisión"""
        return self.truth - self.falsehood

def analisis_neutrosofico_profesores(datos_profesores):
    # Estructura de materias con sus preguntas
    materias = utils_academico.arreglo_materias()
    resultados = []
    for datos in datos_profesores:
        for materia, preguntas in materias.items():
            respuestas = [datos[p] for p in preguntas if p in datos]
            if not respuestas:
                continue
            # Normalizar respuestas de 1-5 a [0,1]
            respuestas_normalizadas = [(r - 1) / 4 for r in respuestas]
            promedio = sum(respuestas_normalizadas) / len(respuestas_normalizadas)
            indeterminacion = 1 - (max(respuestas_normalizadas) - min(respuestas_normalizadas)) / 1 if len(respuestas_normalizadas) > 1 else 0.5
            falsedad = 1 - promedio
            svnn = SingleValuedNeutrosophicNumber(
                id=f"{datos['profesor__nombre']}_{materia}",
                truth=promedio,
                indeterminacy=indeterminacion,
                falsehood=falsedad
            )
            resultados.append({
                'profesor': datos['profesor__nombre'],
                'materia': materia,
                'T': round(svnn.truth, 3),
                'I': round(svnn.indeterminacy, 3),
                'F': round(svnn.falsehood, 3),
                'score': round(svnn.score(), 3),
                'deneutrosophy': round(svnn.deneutrosophy(), 3)
            })
    return resultados

def analisis_neutrosofico_estudiantes(encuestas):
    # Agrupar encuestas por profesor y asignatura
    resultados = {}
    for encuesta in encuestas:
        profesor = encuesta['profesor__nombre']
        materia = encuesta['asignatura__nombre']
        clave = (profesor, materia)
        if clave not in resultados:
            resultados[clave] = []
        preguntas = [
            encuesta['pregunta_1'], encuesta['pregunta_2'], encuesta['pregunta_3'], encuesta['pregunta_4'],
            encuesta['pregunta_5'], encuesta['pregunta_6'], encuesta['pregunta_7'], encuesta['pregunta_8'],
            encuesta['pregunta_9'], encuesta['pregunta_10'], encuesta['pregunta_11']
        ]
        resultados[clave].extend(preguntas)
    calificaciones = []
    for (profesor, materia), respuestas in resultados.items():
        if not respuestas:
            continue
        # Normalizar respuestas de 1-5 a [0,1]
        respuestas_normalizadas = [(r - 1) / 4 for r in respuestas]
        promedio = sum(respuestas_normalizadas) / len(respuestas_normalizadas)
        indeterminacion = 1 - (max(respuestas_normalizadas) - min(respuestas_normalizadas)) / 1 if len(respuestas_normalizadas) > 1 else 0.5
        falsedad = 1 - promedio
        svnn = SingleValuedNeutrosophicNumber(
            id=f"{profesor}_{materia}",
            truth=promedio,
            indeterminacy=indeterminacion,
            falsehood=falsedad
        )
        calificaciones.append({
            'profesor': profesor,
            'materia': materia,
            'T': round(svnn.truth, 3),
            'I': round(svnn.indeterminacy, 3),
            'F': round(svnn.falsehood, 3),
            'score': round(svnn.score(), 3),
            'deneutrosophy': round(svnn.deneutrosophy(), 3)
        })
    return calificaciones 