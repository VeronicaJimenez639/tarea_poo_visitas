from typing import List, Optional
from modelos.visitante import Visitante

class VisitaServicio:
    def __init__(self):
        # Aquí se guarda la lista de visitantes de forma interna.
        # El guion bajo indica que no debe manipularse directamente desde fuera.
        self._lista_visitantes: List[Visitante] = []

    def registrar_visitante(self, visitante_nuevo: Visitante) -> None:
        # Antes de registrar, se verifica si ya existe un visitante con la misma cédula.
        visitante_existente = self._buscar_visitante_por_cedula(visitante_nuevo.cedula)

        if visitante_existente is not None:
            raise ValueError(
                f"Ya existe un visitante registrado con la cédula {visitante_nuevo.cedula}."
            )

        # Si no existe repetido, se agrega a la lista.
        self._lista_visitantes.append(visitante_nuevo)

