# app/gestor_encuestas.py

from encuesta import Encuesta
from pregunta import Pregunta

class GestorEncuestas:
    def __init__(self):
        self.encuestas = []

    def crear_encuesta(self, titulo):
        encuesta = Encuesta(titulo)
        self.encuestas.append(encuesta)
        return encuesta

    def listar_encuestas(self):
        return self.encuestas

    def obtener_encuesta(self, indice):
        return self.encuestas[indice]

    # Métodos relacionados con preguntas
    def listar_preguntas(self):
        return Pregunta.obtener_preguntas_predeterminadas()

    def agregar_pregunta(self, texto):
        nueva_pregunta = Pregunta(texto)
        Pregunta.agregar_pregunta(nueva_pregunta)

    def editar_pregunta(self, indice, nuevo_texto):
        Pregunta.editar_pregunta(indice, nuevo_texto)
