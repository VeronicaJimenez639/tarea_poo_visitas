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

    def _crear_componentes(self):
        # ---------- Formulario ----------
        frame_formulario = tk.Frame(self, padx=15, pady=15) 
        frame_formulario.pack(fill="x")

        etiqueta_cedula = tk.Label(frame_formulario, text="Cédula:")
        etiqueta_cedula.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entrada_cedula = tk.Entry(frame_formulario, width=25)
        self.entrada_cedula.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        etiqueta_nombre = tk.Label(frame_formulario, text="Nombre completo:")
        etiqueta_nombre.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.entrada_nombre_completo = tk.Entry(frame_formulario, width=35)
        self.entrada_nombre_completo.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        etiqueta_motivo = tk.Label(frame_formulario, text="Motivo de visita:")
        etiqueta_motivo.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.entrada_motivo_visita = tk.Entry(frame_formulario, width=70)
        self.entrada_motivo_visita.grid(
            row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w"
        )

        # ---------- Botones ----------
        frame_botones = tk.Frame(self, padx=15, pady=5)
        frame_botones.pack(fill="x")

        boton_registrar = tk.Button(
            frame_botones,
            text="Registrar",
            width=15,
            command=self._registrar_visitante
        )
        boton_registrar.pack(side=tk.LEFT, padx=5)

        boton_actualizar = tk.Button(
            frame_botones,
            text="Actualizar",
            width=15,
            command=self._actualizar_visitante
        )
        boton_actualizar.pack(side=tk.LEFT, padx=5)

        boton_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            width=15,
            command=self._eliminar_visitante
        )
        boton_eliminar.pack(side=tk.LEFT, padx=5)

        boton_limpiar = tk.Button(
            frame_botones,
            text="Limpiar campos",
            width=15,
            command=self._limpiar_campos
        )
        boton_limpiar.pack(side=tk.LEFT, padx=5)

        # ---------- Tabla ----------
        frame_tabla = tk.Frame(self, padx=15, pady=15)
        frame_tabla.pack(fill="both", expand=True)

        columnas = ("cedula", "nombre_completo", "motivo_visita")
        self.tabla_visitantes = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=12
        )

        # Encabezados de la tabla.
        self.tabla_visitantes.heading("cedula", text="Cédula")
        self.tabla_visitantes.heading("nombre_completo", text="Nombre completo")
        self.tabla_visitantes.heading("motivo_visita", text="Motivo de visita")

        # Ancho de las columnas.
        self.tabla_visitantes.column("cedula", width=150)
        self.tabla_visitantes.column("nombre_completo", width=250)
        self.tabla_visitantes.column("motivo_visita", width=350)

        self.tabla_visitantes.pack(fill="both", expand=True)

        # Evento que permite cargar en el formulario los datos seleccionados.
        self.tabla_visitantes.bind("<<TreeviewSelect>>", self._cargar_datos_seleccionados)

    def _registrar_visitante(self):
        # Obtiene los datos escritos en los campos.
        cedula = self.entrada_cedula.get().strip()
        nombre_completo = self.entrada_nombre_completo.get().strip()
        motivo_visita = self.entrada_motivo_visita.get().strip()

        try:
            # Se crea el objeto visitante con los datos ingresados.
            visitante_nuevo = Visitante(cedula, nombre_completo, motivo_visita)

            # Se envía al servicio para registrarlo.
            self.visita_servicio.registrar_visitante(visitante_nuevo)

            # Se actualiza la tabla y se limpian los campos.
            self._actualizar_tabla_visitantes()
            self._limpiar_campos()

            messagebox.showinfo("Registro exitoso", "El visitante fue registrado correctamente.")
        except ValueError as error:
            # Si ocurre una validación incorrecta, se muestra una advertencia.
            messagebox.showwarning("Atención", str(error))

