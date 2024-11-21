# app/pregunta.py

class Pregunta:
    banco_preguntas = [
        "¿Cómo califica nuestro servicio?",
        "¿Volvería a elegirnos?",
        "¿Recomendaría nuestros servicios?"
    ]

    def __init__(self, texto):
        self.texto = texto

    @staticmethod
    def obtener_preguntas_predeterminadas():
        """
        Devuelve una lista de instancias de Pregunta a partir del banco de preguntas.
        """
        return [Pregunta(texto) for texto in Pregunta.banco_preguntas]

    @staticmethod
    def agregar_pregunta(pregunta):
        """
        Agrega una nueva pregunta al banco de preguntas.
        """
        if isinstance(pregunta, Pregunta):
            Pregunta.banco_preguntas.append(pregunta.texto)

    @staticmethod
    def editar_pregunta(indice, nuevo_texto):
        """
        Edita una pregunta del banco de preguntas por su índice.
        """
        if 0 <= indice < len(Pregunta.banco_preguntas):
            Pregunta.banco_preguntas[indice] = nuevo_texto
