import pandas as pd
from academico.models import Profesor, Estudiante, EncuestaProfesor, EncuestaEstudiante, Asignatura

def cargar_encuesta_profesores_desde_excel(archivo):
    try:
        data = pd.read_excel(archivo)
        for index, row in data.iterrows():
            profesor, _ = Profesor.objects.get_or_create(nombre=row['¿Cuál es su nombre?'])

            nombre_profesor=row['¿Cuál es su nombre?']
            rango_edad=row['Rango de edad al que pertenece']
            nivel_educacion=row['¿Cuál es su nivel de educación?']
            titulo_relacionado=normalizar_respuesta_boolean(row['¿Su titulo profesional esta relacionado con el área de enseñanza que imparte?'])
            cursos_pedagogicos=normalizar_respuesta_boolean(row['¿Ha tomado cursos de capacitación pedagógica?'])
            reconocimientos_academicos=normalizar_respuesta_boolean(row['¿Ha recibido algún reconocimiento académico en su carrera docente?'])
            preferencias_asignaturas=row['Escoja de acuerdo a sus preferencias, las asignaturas que desee impartir.']
            metodologias_ensenanza=row['¿Qué metodologías de enseñanza prefiere utilizar en sus clases?']
            materias_impartidas=row['¿Qué materias dentro del campo de Software usted ha impartido?']
            veces_impartidas=row['En base a la pregunta anterior ¿Cuántas veces usted ha sido elegido para dar esas materias? Elija las materias']
            acepta_sistema_recomendacion=normalizar_respuesta(row['¿Está de acuerdo con la implementación de un sistema de recomendación que sugiera la asignatura que debe dar un Docente?'], '¿Está de acuerdo con la implementación de un sistema de recomendación que sugiera la asignatura que debe dar un Docente?', index + 2)
            materias_no_relacionadas=normalizar_respuesta(row['¿Considera que las materias que le han tocado impartir no están de acuerdo con su formación profesional?'], '¿Considera que las materias que le han tocado impartir no están de acuerdo con su formación profesional?', index + 2)
            desacuerdo_con_materias=normalizar_respuesta(row['¿Alguna vez se ha sentido en desacuerdo con la materia que debió impartir?'], '¿Alguna vez se ha sentido en desacuerdo con la materia que debió impartir?', index + 2)
            conoce_sistemas_recomendacion=normalizar_respuesta(row['¿Usted ha escuchado o leído sobre los Sistemas de Recomendación?'], '¿Usted ha escuchado o leído sobre los Sistemas de Recomendación?', index + 2)
            cree_en_sistemas_recomendacion=normalizar_respuesta(row['¿Cree usted que un Sistema de Recomendación pueda sugerir la materia idónea acorde a su perfil docente?'], '¿Cree usted que un Sistema de Recomendación pueda sugerir la materia idónea acorde a su perfil docente?', index + 2)
            acepta_implementacion=normalizar_respuesta(row['¿Estaría de acuerdo con la implementación de un Sistema de Recomendación para la carrera de Software?'], '¿Estaría de acuerdo con la implementación de un Sistema de Recomendación para la carrera de Software?', index + 2)

            introduccion_pregunta_1=normalizar_respuesta(row['¿Cómo calificaría su familiaridad con los principios básicos de la ingeniería de software, incluyendo el ciclo de vida del software, procesos y modelos?'], '¿Cómo calificaría su familiaridad con los principios básicos de la ingeniería de software, incluyendo el ciclo de vida del software, procesos y modelos?', index + 2)
            introduccion_pregunta_2=normalizar_respuesta(row['¿Qué tan preparado se siente para impartir la materia de Introducción a Ingeniería de Software, considerando su experiencia y conocimientos en el área?'], '¿Qué tan preparado se siente para impartir la materia de Introducción a Ingeniería de Software, considerando su experiencia y conocimientos en el área?', index + 2)
            introduccion_pregunta_3=normalizar_respuesta(row['¿Qué tan familiarizado se siente con el proceso de resolución de problemas, incluyendo la identificación de datos de entrada, procesos y salidas?'], '¿Qué tan familiarizado se siente con el proceso de resolución de problemas, incluyendo la identificación de datos de entrada, procesos y salidas?', index + 2)

            proceso_software_pregunta_1=normalizar_respuesta(row['¿Cómo calificaría su experiencia en la implementación de procesos de software, como Scrum, Waterfall o DevOps?'], '¿Cómo calificaría su experiencia en la implementación de procesos de software, como Scrum, Waterfall o DevOps?', index + 2)
            proceso_software_pregunta_2=normalizar_respuesta(row['¿Cómo calificaría su conocimiento sobre normativas y estándares internacionales de procesos de software (como CMMI, ISO 9001, etc.)?'], '¿Cómo calificaría su conocimiento sobre normativas y estándares internacionales de procesos de software (como CMMI, ISO 9001, etc.)?', index + 2)
            proceso_software_pregunta_3=normalizar_respuesta(row['¿Con qué frecuencia ha realizado publicaciones o trabajos de investigación en temas relacionados con la mejora de procesos de software?'], '¿Con qué frecuencia ha realizado publicaciones o trabajos de investigación en temas relacionados con la mejora de procesos de software?', index + 2)

            ing_requerimientos_pregunta_1=normalizar_respuesta(row['¿Qué tan frecuentemente ha participado en proyectos donde se han identificado y documentado requerimientos?'], '¿Qué tan frecuentemente ha participado en proyectos donde se han identificado y documentado requerimientos?', index + 2)
            ing_requerimientos_pregunta_2=normalizar_respuesta(row['¿Qué tan competente se siente en el uso de técnicas como entrevistas, encuestas y análisis de stakeholders para la recopilación de información?'], '¿Qué tan competente se siente en el uso de técnicas como entrevistas, encuestas y análisis de stakeholders para la recopilación de información?', index + 2)
            ing_requerimientos_pregunta_3=normalizar_respuesta(row['¿Qué tan hábil se considera al interactuar con clientes y equipos multidisciplinarios para comprender y definir requerimientos?'], '¿Qué tan hábil se considera al interactuar con clientes y equipos multidisciplinarios para comprender y definir requerimientos?', index + 2)

            model_software_pregunta_1=normalizar_respuesta(row['¿Qué tan familiarizado se siente con el uso de UML, BPMN u otras herramientas similares para la modelación de procesos y requerimientos?'], '¿Qué tan familiarizado se siente con el uso de UML, BPMN u otras herramientas similares para la modelación de procesos y requerimientos?', index + 2)
            model_software_pregunta_2=normalizar_respuesta(row['¿Cuál es su nivel de experiencia en el uso de herramientas de diseño y modelado, como Enterprise Architect, Visual Paradigm, entre otras?'], '¿Cuál es su nivel de experiencia en el uso de herramientas de diseño y modelado, como Enterprise Architect, Visual Paradigm, entre otras?', index + 2)
            model_software_pregunta_3=normalizar_respuesta(row['¿Qué tan frecuentemente ha participado en proyectos de modelado de software a gran escala o que involucren arquitecturas complejas?'], '¿Qué tan frecuentemente ha participado en proyectos de modelado de software a gran escala o que involucren arquitecturas complejas?', index + 2)

            dise_arqui_software_pregunta_1=normalizar_respuesta(row['¿Cuál es su nivel de experiencia en el diseño de arquitecturas de software en proyectos reales, incluyendo arquitecturas monolíticas, distribuidas y de microservicios?'], '¿Cuál es su nivel de experiencia en el diseño de arquitecturas de software en proyectos reales, incluyendo arquitecturas monolíticas, distribuidas y de microservicios?', index + 2)
            dise_arqui_software_pregunta_2=normalizar_respuesta(row['¿Qué tan familiarizado está con patrones de arquitectura de software, como MVC, MVVM, Singleton, entre otros?'], '¿Qué tan familiarizado está con patrones de arquitectura de software, como MVC, MVVM, Singleton, entre otros?', index + 2)
            dise_arqui_software_pregunta_3=normalizar_respuesta(row['¿Qué tan preparado se siente para enseñar sobre la selección de arquitecturas de software adecuadas, considerando los requerimientos del sistema y las limitaciones del entorno?'], '¿Qué tan preparado se siente para enseñar sobre la selección de arquitecturas de software adecuadas, considerando los requerimientos del sistema y las limitaciones del entorno?', index + 2)

            hombre_maquina_pregunta_1=normalizar_respuesta(row['¿Se siente capacitado para impartir una materia sobre diseño de interfaces gráficas de usuario (GUI) y experiencia de usuario (UX) basada en su experiencia y conocimientos en estas áreas?'], '¿Se siente capacitado para impartir una materia sobre diseño de interfaces gráficas de usuario (GUI) y experiencia de usuario (UX) basada en su experiencia y conocimientos en estas áreas?', index + 2)
            hombre_maquina_pregunta_2=normalizar_respuesta(row['¿Usted posee conocimiento en principios de usabilidad, accesibilidad y diseño centrado en el usuario?'], '¿Usted posee conocimiento en principios de usabilidad, accesibilidad y diseño centrado en el usuario?', index + 2)
            hombre_maquina_pregunta_3=normalizar_respuesta(row['¿Qué tan preparado consideras que está el docente para impartir clases sobre el uso de herramientas de diseño como Sketch, Figma y Adobe XD?'], '¿Qué tan preparado consideras que está el docente para impartir clases sobre el uso de herramientas de diseño como Sketch, Figma y Adobe XD?', index + 2)

            construccion_software_pregunta_1=normalizar_respuesta(row['¿Qué tan cómodo te sientes impartiendo clases sobre desarrollo de software utilizando diversas tecnologías y lenguajes de programación?'], '¿Qué tan cómodo te sientes impartiendo clases sobre desarrollo de software utilizando diversas tecnologías y lenguajes de programación?', index + 2)
            construccion_software_pregunta_2=normalizar_respuesta(row['¿Cuál es tu nivel de conocimiento y experiencia en el trabajo con metodologías ágiles como Scrum, Kanban u otras?'], '¿Cuál es tu nivel de conocimiento y experiencia en el trabajo con metodologías ágiles como Scrum, Kanban u otras?', index + 2)
            construccion_software_pregunta_3=normalizar_respuesta(row['¿Cómo evaluarías tu capacidad para aplicar buenas prácticas de desarrollo, como el uso de patrones de diseño, principios SOLID y el refactoring?'], '¿Cómo evaluarías tu capacidad para aplicar buenas prácticas de desarrollo, como el uso de patrones de diseño, principios SOLID y el refactoring?', index + 2)

            experiencia_usuario_pregunta_1=normalizar_respuesta(row['¿Cómo calificarías tu experiencia en el diseño de interfaces que favorezcan la experiencia del usuario?'], '¿Cómo calificarías tu experiencia en el diseño de interfaces que favorezcan la experiencia del usuario?', index + 2)
            experiencia_usuario_pregunta_2=normalizar_respuesta(row['¿Cómo evaluarías tu capacidad para realizar pruebas de usabilidad, llevar a cabo entrevistas con usuarios y analizar datos relacionados con la experiencia del usuario?'], '¿Cómo evaluarías tu capacidad para realizar pruebas de usabilidad, llevar a cabo entrevistas con usuarios y analizar datos relacionados con la experiencia del usuario?', index + 2)
            experiencia_usuario_pregunta_3=normalizar_respuesta(row['¿Cómo calificarías tu capacidad para evaluar y aplicar buenas prácticas de desarrollo, tales como el uso de patrones de diseño, la implementación de los principios SOLID y la realización de refactoring en tus proyectos?'], '¿Cómo calificarías tu capacidad para evaluar y aplicar buenas prácticas de desarrollo, tales como el uso de patrones de diseño, la implementación de los principios SOLID y la realización de refactoring en tus proyectos?', index + 2)

            configuracion_software_pregunta_1=normalizar_respuesta(row['¿Considera que su experiencia profesional facilita la enseñanza de herramientas de control de versiones?'], '¿Considera que su experiencia profesional facilita la enseñanza de herramientas de control de versiones?', index + 2)
            configuracion_software_pregunta_2=normalizar_respuesta(row['¿Cree que su experiencia laboral ayuda a explicar la importancia de la gestión de cambios en proyectos reales?'], '¿Cree que su experiencia laboral ayuda a explicar la importancia de la gestión de cambios en proyectos reales?', index + 2)
            configuracion_software_pregunta_3=normalizar_respuesta(row['¿Piensa que sus conocimientos prácticos mejoran la comprensión de los estudiantes sobre la gestión de la configuración?'], '¿Piensa que sus conocimientos prácticos mejoran la comprensión de los estudiantes sobre la gestión de la configuración?', index + 2)

            calidad_software_pregunta_1=normalizar_respuesta(row['¿Cómo calificarías tu conocimiento y experiencia en la implementación de pruebas de software, incluyendo pruebas unitarias, de integración, de sistema y de aceptación?'], '¿Cómo calificarías tu conocimiento y experiencia en la implementación de pruebas de software, incluyendo pruebas unitarias, de integración, de sistema y de aceptación?', index + 2)
            calidad_software_pregunta_2=normalizar_respuesta(row['¿Cuál es tu nivel de familiaridad con herramientas de automatización de pruebas, como Selenium, JUnit, TestNG, entre otras?'], '¿Cuál es tu nivel de familiaridad con herramientas de automatización de pruebas, como Selenium, JUnit, TestNG, entre otras?', index + 2)
            calidad_software_pregunta_3=normalizar_respuesta(row['¿Cuál es tu nivel de conocimiento sobre modelos de calidad de software, como TMMi (Test Maturity Model integration) o ISO/IEC 25010?'], '¿Cuál es tu nivel de conocimiento sobre modelos de calidad de software, como TMMi (Test Maturity Model integration) o ISO/IEC 25010?', index + 2)

            validacion_software_pregunta_1=normalizar_respuesta(row['¿Cuál es tu nivel de dominio en el uso de herramientas de control de versiones, como Git, SVN, entre otras?'], '¿Cuál es tu nivel de dominio en el uso de herramientas de control de versiones, como Git, SVN, entre otras?', index + 2)
            validacion_software_pregunta_2=normalizar_respuesta(row['Cuál es tu nivel de familiaridad con herramientas de integración continua y despliegue, como Jenkins, GitLab CI, CircleCI, entre otras?'], 'Cuál es tu nivel de familiaridad con herramientas de integración continua y despliegue, como Jenkins, GitLab CI, CircleCI, entre otras?', index + 2)
            validacion_software_pregunta_3=normalizar_respuesta(row['¿Cuál es tu nivel de experiencia con herramientas de automatización y gestión de configuración, como Ansible, Puppet, Chef, entre otras?'], '¿Cuál es tu nivel de experiencia con herramientas de automatización y gestión de configuración, como Ansible, Puppet, Chef, entre otras?', index + 2)

            auditoria_software_pregunta_1=normalizar_respuesta(row['¿Cuál es tu nivel de familiaridad con normativas internacionales y procesos de auditoría de software, como ISO/IEC 27001, CMMI, ITIL, entre otras?'], '¿Cuál es tu nivel de familiaridad con normativas internacionales y procesos de auditoría de software, como ISO/IEC 27001, CMMI, ITIL, entre otras?', index + 2)
            auditoria_software_pregunta_2=normalizar_respuesta(row['¿Cuál es tu nivel de experiencia en la realización de auditorías de código, documentación y procesos de desarrollo de software?'], '¿Cuál es tu nivel de experiencia en la realización de auditorías de código, documentación y procesos de desarrollo de software?', index + 2)
            auditoria_software_pregunta_3=normalizar_respuesta(row['¿Cómo evaluarías tu capacidad de análisis crítico y detección de posibles fallos o inconsistencias en el proceso de desarrollo de software?'], '¿Cómo evaluarías tu capacidad de análisis crítico y detección de posibles fallos o inconsistencias en el proceso de desarrollo de software?', index + 2)
            # proceso_software_procesos_software = row['Experiencia en la implementación de procesos de software, como Scrum, Waterfall, o DevOps. ']
            # proceso_software_procesos_software = (
            #     normalize_likert(proceso_software_procesos_software, 0, 10)  # Normaliza si es numérico
            #     if isinstance(proceso_software_procesos_software, (int, float))
            #     else likert_mapping.get(proceso_software_procesos_software, 3)  # Mapea si es texto; por defecto 3
            # )

            EncuestaProfesor.objects.create(
                profesor=profesor,

                nombre_profesor=nombre_profesor,
                rango_edad=rango_edad,
                nivel_educacion=nivel_educacion,
                titulo_relacionado=titulo_relacionado,
                cursos_pedagogicos=cursos_pedagogicos,
                reconocimientos_academicos=reconocimientos_academicos,
                preferencias_asignaturas=preferencias_asignaturas,
                metodologias_ensenanza=metodologias_ensenanza,
                materias_impartidas=materias_impartidas,
                veces_impartidas=veces_impartidas,
                acepta_sistema_recomendacion=acepta_sistema_recomendacion,
                materias_no_relacionadas=materias_no_relacionadas,
                desacuerdo_con_materias=desacuerdo_con_materias,
                conoce_sistemas_recomendacion=conoce_sistemas_recomendacion,
                cree_en_sistemas_recomendacion=cree_en_sistemas_recomendacion,
                acepta_implementacion=acepta_implementacion,

                # ? Introducción a la ingenieria de Software
                introduccion_pregunta_1=introduccion_pregunta_1,
                introduccion_pregunta_2=introduccion_pregunta_2,
                introduccion_pregunta_3=introduccion_pregunta_3,
                # ? Proceso de Software
                proceso_software_pregunta_1=proceso_software_pregunta_1,
                proceso_software_pregunta_2=proceso_software_pregunta_2,
                proceso_software_pregunta_3=proceso_software_pregunta_3,
                # ? Ingenieria de Requerimientos
                ing_requerimientos_pregunta_1=ing_requerimientos_pregunta_1,
                ing_requerimientos_pregunta_2=ing_requerimientos_pregunta_2,
                ing_requerimientos_pregunta_3=ing_requerimientos_pregunta_3,
                # ? Modelamiento de Software
                model_software_pregunta_1=model_software_pregunta_1,
                model_software_pregunta_2=model_software_pregunta_2,
                model_software_pregunta_3=model_software_pregunta_3,
                # ? Diseño y arquitectura de Software
                dise_arqui_software_pregunta_1=dise_arqui_software_pregunta_1,
                dise_arqui_software_pregunta_2=dise_arqui_software_pregunta_2,
                dise_arqui_software_pregunta_3=dise_arqui_software_pregunta_3,
                # ? Interacción Hombre-maquina
                hombre_maquina_pregunta_1=hombre_maquina_pregunta_1,
                hombre_maquina_pregunta_2=hombre_maquina_pregunta_2,
                hombre_maquina_pregunta_3=hombre_maquina_pregunta_3,
                # ? Construccion de Software
                construccion_software_pregunta_1=construccion_software_pregunta_1,
                construccion_software_pregunta_2=construccion_software_pregunta_2,
                construccion_software_pregunta_3=construccion_software_pregunta_3,
                # ? Diseño y experiencia de Usuario
                experiencia_usuario_pregunta_1=experiencia_usuario_pregunta_1,
                experiencia_usuario_pregunta_2=experiencia_usuario_pregunta_2,
                experiencia_usuario_pregunta_3=experiencia_usuario_pregunta_3,
                # ? Calidad de Software
                calidad_software_pregunta_1=calidad_software_pregunta_1,
                calidad_software_pregunta_2=calidad_software_pregunta_2,
                calidad_software_pregunta_3=calidad_software_pregunta_3,
                # ? Verificación y validacion de Software
                validacion_software_pregunta_1=validacion_software_pregunta_1,
                validacion_software_pregunta_2=validacion_software_pregunta_2,
                validacion_software_pregunta_3=validacion_software_pregunta_3,
                # ? Gestion de la configuración del Software
                configuracion_software_pregunta_1=configuracion_software_pregunta_1,
                configuracion_software_pregunta_2=configuracion_software_pregunta_2,
                configuracion_software_pregunta_3=configuracion_software_pregunta_3,
                # ? Auditoria de Software
                auditoria_software_pregunta_1=auditoria_software_pregunta_1,
                auditoria_software_pregunta_2=auditoria_software_pregunta_2,
                auditoria_software_pregunta_3=auditoria_software_pregunta_3,
            )
    except Exception as e:
        raise # Re-lanza la excepción para que se maneje en la vista



def cargar_encuesta_estudiantes_desde_excel(archivo):
    data = pd.read_excel(archivo)
    for index, row in data.iterrows():
        estudiante, _ = Estudiante.objects.get_or_create(correo=row['Dirección de correo electrónico'])
        asignatura, _ = Asignatura.objects.get_or_create(nombre=row['Elige la materia'])
        profesor, _ = Profesor.objects.get_or_create(nombre=row['Elige el docente'].upper())

        pregunta_1=normalizar_respuesta(row['El docente presenta de manera clara y comprensible los conceptos fundamentales de la ingeniería de software.'], 'El docente presenta de manera clara y comprensible los conceptos fundamentales de la ingeniería de software.', index + 2)
        pregunta_2=normalizar_respuesta(row['El docente fomenta la participación activa de los estudiantes durante las clases.'], 'El docente fomenta la participación activa de los estudiantes durante las clases.', index + 2)
        pregunta_3=normalizar_respuesta(row['El docente utiliza ejemplos prácticos y reales para explicar los conceptos.'], 'El docente utiliza ejemplos prácticos y reales para explicar los conceptos.', index + 2)
        pregunta_4=normalizar_respuesta(row['El docente responde oportunamente las dudas planteadas durante las clases.'], 'El docente responde oportunamente las dudas planteadas durante las clases.', index + 2)
        pregunta_5=normalizar_respuesta(row['Las evaluaciones reflejan los contenidos y habilidades enseñadas en clase.'], 'Las evaluaciones reflejan los contenidos y habilidades enseñadas en clase.', index + 2)
        pregunta_6=normalizar_respuesta(row['El docente está disponible fuera del horario de clase para resolver dudas o apoyar con el aprendizaje.'], 'El docente está disponible fuera del horario de clase para resolver dudas o apoyar con el aprendizaje.', index + 2)
        pregunta_7=normalizar_respuesta(row['El docente utiliza recursos multimedia (videos, presentaciones, etc.) que enriquecen el aprendizaje.'], 'El docente utiliza recursos multimedia (videos, presentaciones, etc.) que enriquecen el aprendizaje.', index + 2)
        pregunta_8=normalizar_respuesta(row['El docente establece expectativas claras sobre el trabajo y las evaluaciones desde el inicio del curso.'], 'El docente establece expectativas claras sobre el trabajo y las evaluaciones desde el inicio del curso.', index + 2)
        pregunta_9=normalizar_respuesta(row['¿El docente durante su clase fomenta el trabajo en equipo?'], '¿El docente durante su clase fomenta el trabajo en equipo?', index + 2)
        pregunta_10=normalizar_respuesta(row['Las clases tienen un enfoque práctico que facilita la comprensión de los conceptos.'], 'Las clases tienen un enfoque práctico que facilita la comprensión de los conceptos.', index + 2)
        pregunta_11=normalizar_respuesta(row['Las clases tienen un enfoque práctico que facilita la comprensión de los conceptos.'], 'Las clases tienen un enfoque práctico que facilita la comprensión de los conceptos.', index + 2)

        EncuestaEstudiante.objects.create(
            estudiante=estudiante,
            asignatura=asignatura,
            profesor=profesor,
            pregunta_1=pregunta_1,
            pregunta_2=pregunta_2,
            pregunta_3=pregunta_3,
            pregunta_4=pregunta_4,
            pregunta_5=pregunta_5,
            pregunta_6=pregunta_6,
            pregunta_7=pregunta_7,
            pregunta_8=pregunta_8,
            pregunta_9=pregunta_9,
            pregunta_10=pregunta_10,
            pregunta_11=pregunta_11,
            
        )


#Formula de likert
def normalize_likert(value, original_min, original_max):
    return 1 + 4 * (value - original_min) / (original_max - original_min)


# Respuesta boolean
def normalizar_respuesta_boolean(respuesta):
    return respuesta.upper() == 'SI'


def normalizar_respuesta(respuesta, columna, fila):
    if pd.isna(respuesta):
        raise ValueError(f"Error en la FILA {fila} PREGUNTA {columna} no puede ser vacío o NaN.")
    """Normaliza la respuesta según su tipo (numérico o texto)."""
    if isinstance(respuesta, (int, float)):
        return normalize_likert(respuesta, 0, 10)  # Normaliza si es numérico
    return likert_mapping.get(respuesta, 3)  # Mapea si es texto; por defecto 3


likert_mapping = {
    # ! 1
    "Muy malo": 1,
    "Muy bajo": 1,
    "Muy poco": 1,
    "Nunca": 1,
    "Ninguna": 1,
    "Totalmente en desacuerdo": 1,
    "No": 1,
    # ! 2
    "Malo": 2,
    "Bajo": 2,
    "Poco": 2,
    "Poca": 2,
    "Casi nunca": 2,
    "Rara vez": 2,
    "En desacuerdo": 2,
    # ! 3
    "Regular": 3,
    "Moderado": 3,
    "Moderada": 3,
    "Moderadamente": 3,
    "Neutral": 3,
    "Aveces": 3,
    "A veces": 3,
    "Tal vez": 3,
    "Ni de acuerdo ni en desacuerdo": 3,
    # ! 4
    "Bueno": 4,
    "Buena": 4,
    "Alto": 4,
    "Alta": 4,
    "Prepado": 4,
    "Casi siempre": 4,
    "Frecuentemente": 4,
    "Competente": 4,
    "Familiarizado": 4,
    "Bastante": 4,
    "De acuerdo": 4,
    # ! 5
    "Excelente": 5,
    "Muy buena": 5,
    "Muy bueno": 5,
    "Muy alto": 5,
    "Muy alta": 5,
    "Muy preparado": 5,
    "Siempre": 5,
    "Muy competente": 5,
    "Muy familiarizado": 5,
    "Totalmente de acuerdo": 5,
    "Si": 5,
}