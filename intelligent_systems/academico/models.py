from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    correo = models.CharField(max_length=255)

    def __str__(self):
        return self.correo


class EncuestaProfesor(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    nombre_profesor = models.CharField(max_length=50)
    rango_edad = models.CharField(max_length=50)
    nivel_educacion = models.CharField(max_length=50)
    titulo_relacionado = models.BooleanField()
    cursos_pedagogicos = models.BooleanField()
    reconocimientos_academicos = models.BooleanField()
    preferencias_asignaturas = models.TextField()  
    metodologias_ensenanza = models.TextField()
    acepta_sistema_recomendacion = models.PositiveIntegerField(default=1)  # 1-5
    materias_impartidas = models.TextField()
    veces_impartidas = models.TextField()
    materias_no_relacionadas = models.PositiveIntegerField(default=1)  # 1-5
    desacuerdo_con_materias = models.PositiveIntegerField(default=1)  # 1-5
    conoce_sistemas_recomendacion = models.PositiveIntegerField(default=1)  # 1-5
    cree_en_sistemas_recomendacion = models.PositiveIntegerField(default=1)  # 1-5
    acepta_implementacion = models.PositiveIntegerField(default=1)  # 1-5

    # ! Preguntas relacionadas a experiencia en materias
    # ? Introducción a la ingenieria de Software
    introduccion_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    introduccion_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    introduccion_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    # ? Proceso de Software
    proceso_software_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    proceso_software_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    proceso_software_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    # ? Ingenieria de Requerimientos
    ing_requerimientos_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    ing_requerimientos_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    ing_requerimientos_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    # ? Modelamiento de Software
    model_software_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    model_software_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    model_software_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    # ? Diseño y arquitectura de Software
    dise_arqui_software_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    dise_arqui_software_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    dise_arqui_software_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    # ? Interacción Hombre-maquina
    hombre_maquina_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    hombre_maquina_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    hombre_maquina_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    # ? Construccion de Software
    construccion_software_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    construccion_software_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    construccion_software_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    # ? Diseño y experiencia de Usuario
    experiencia_usuario_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    experiencia_usuario_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    experiencia_usuario_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    # ? Calidad de Software
    calidad_software_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    calidad_software_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    calidad_software_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    # ? Verificación y validacion de Software
    validacion_software_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    validacion_software_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    validacion_software_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    # ? Gestion de la configuración del Software
    configuracion_software_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    configuracion_software_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    configuracion_software_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    # ? Auditoria de Software
    auditoria_software_pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    auditoria_software_pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    auditoria_software_pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5

    def __str__(self):
        return f"Encuesta de {self.profesor.nombre}"


class EncuestaEstudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    pregunta_1 = models.PositiveIntegerField(default=1)  # 1-5
    pregunta_2 = models.PositiveIntegerField(default=1)  # 1-5
    pregunta_3 = models.PositiveIntegerField(default=1)  # 1-5
    pregunta_4 = models.PositiveIntegerField(default=1)  # 1-5
    pregunta_5 = models.PositiveIntegerField(default=1)  # 1-5
    pregunta_6 = models.PositiveIntegerField(default=1)  # 1-5
    pregunta_7 = models.PositiveIntegerField(default=1)  # 1-5
    pregunta_8 = models.PositiveIntegerField(default=1)  # 1-5
    pregunta_9 = models.PositiveIntegerField(default=1)  # 1-5
    pregunta_10 = models.PositiveIntegerField(default=1)  # 1-5
    pregunta_11 = models.PositiveIntegerField(default=1)  # 1-5

    def __str__(self):
        return f"Encuesta de {self.estudiante.correo}"
