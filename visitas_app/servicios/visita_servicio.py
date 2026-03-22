from typing import List, Optional
from modelos.visitante import Visitante

class VisitaServicio:
    def __init__(self):
        # Aquí se guarda la lista de visitantes de forma interna.
        # El guion bajo indica que no debe manipularse directamente desde fuera.
        self._lista_visitantes: List[Visitante] = []

