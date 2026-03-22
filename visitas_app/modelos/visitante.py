class Visitante:
    def __init__(self, cedula: str, nombre_completo: str, motivo_visita: str):
        # Se asignan los valores usando las propiedades para que pasen por validación.
        self.cedula = cedula
        self.nombre_completo = nombre_completo
        self.motivo_visita = motivo_visita