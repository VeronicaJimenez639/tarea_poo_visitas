class Visitante:
    def __init__(self, cedula: str, nombre_completo: str, motivo_visita: str):
        # Se asignan los valores usando las propiedades para que pasen por validación.
        self.cedula = cedula
        self.nombre_completo = nombre_completo
        self.motivo_visita = motivo_visita

    @property
    def cedula(self) -> str:
        # Retorna la cédula del visitante.
        return self._cedula

    @cedula.setter
    def cedula(self, valor: str):
        # Valida que la cédula no esté vacía.
        if not valor or not valor.strip():
            raise ValueError("La cédula no puede estar vacía.")

        # strip() elimina espacios al inicio y al final.
        self._cedula = valor.strip()

    @property
    def nombre_completo(self) -> str:
        # Retorna el nombre completo del visitante.
        return self._nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, valor: str):
        # Valida que el nombre no esté vacío.
        if not valor or not valor.strip():
            raise ValueError("El nombre completo no puede estar vacío.")

        self._nombre_completo = valor.strip()

    @property
    def motivo_visita(self) -> str:
        # Retorna el motivo de la visita.
        return self._motivo_visita

    @motivo_visita.setter
    def motivo_visita(self, valor: str):
        # Valida que el motivo no esté vacío.
        if not valor or not valor.strip():
            raise ValueError("El motivo de la visita no puede estar vacío.")

        self._motivo_visita = valor.strip()         