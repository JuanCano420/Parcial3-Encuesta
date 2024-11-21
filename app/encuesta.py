# app/encuesta.py
class Encuesta:
    def __init__(self, titulo):
        self.titulo = titulo
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
