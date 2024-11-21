"""
Módulo para la generación de informes de encuestas.
"""

class Informe:
    def __init__(self, encuesta):
        self.encuesta = encuesta

    def generar(self):
        print(f"Generando informe para: {self.encuesta.titulo}")
        print("Distribución de respuestas: (Simulación)")
        for pregunta in self.encuesta.preguntas:
            print(f"{pregunta}: 50% Sí, 50% No")
