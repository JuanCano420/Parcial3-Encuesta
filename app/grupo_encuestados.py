"""
Módulo para la gestión de grupos de encuestados.
"""

import csv

class GrupoEncuestados:
    def __init__(self):
        self.encuestados = []

    def importar_csv(self, archivo):
        try:
            with open(archivo, newline='', encoding='utf-8') as csvfile:
                lector = csv.DictReader(csvfile)
                self.encuestados = [fila for fila in lector]
            print(f"Se importaron {len(self.encuestados)} encuestados.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

    def segmentar_por(self, campo, valor):
        segmentados = [e for e in self.encuestados if e.get(campo) == valor]
        print(f"Se encontraron {len(segmentados)} encuestados con {campo} = {valor}.")
        return segmentados
