import tkinter as tk
from tkinter import ttk, messagebox

from modelos.visitante import Visitante


class AppVisitas(tk.Tk):
    def __init__(self, visita_servicio):
        # Se llama al constructor de Tk para inicializar la ventana principal.
        super().__init__()

        # Se recibe el servicio por parámetro.
        # Esto es inyección de dependencias y ayuda a separar UI y lógica.
        self.visita_servicio = visita_servicio

        # Guarda la cédula del registro seleccionado en la tabla.
        self.cedula_seleccionada = None

        # Configuración principal de la ventana.
        self.title("Sistema de Registro de Visitantes")
        self.geometry("800x500")
        self.resizable(False, False)

        # Se crean los componentes de la interfaz.
        self._crear_componentes()

        # Se carga la tabla al iniciar la app.
        self._actualizar_tabla_visitantes()