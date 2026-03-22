from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppVisitas

def main():
    # Se crea la instancia del servicio.
    visita_servicio = VisitaServicio()

    # Se inyecta el servicio dentro de la interfaz gráfica.
    aplicacion = AppVisitas(visita_servicio)

    # Inicia el ciclo principal de la aplicación.
    aplicacion.mainloop()

# Este condicional asegura que main() solo se ejecute
# cuando el archivo se corre directamente.
if __name__ == "__main__":
    main()