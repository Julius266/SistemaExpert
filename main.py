import os
from dotenv import load_dotenv
from tkinter import Tk
from src.interfaz_usuario import InterfazUsuario
from src.diagnostico import Diagnostico, Sintoma

# Cargar las variables de entorno desde .env
load_dotenv()

def enviar_informacion(interfaz):
    usuario = interfaz.obtener_informacion_usuario()
    sintomas = interfaz.obtener_sintomas()

    try:
        motor_diagnostico = Diagnostico()
        motor_diagnostico.reset()
        declarar_sintomas(motor_diagnostico, sintomas)
        motor_diagnostico.run()
        diagnostico = motor_diagnostico.obtener_diagnostico()
        interfaz.imprimir_resultados(usuario, diagnostico)
    except Exception as e:
        interfaz.mostrar_error(f"Ha ocurrido un error: {e}")

def declarar_sintomas(motor_diagnostico, sintomas):
    for sintoma, valor in sintomas.items():
        motor_diagnostico.declare(Sintoma(**{sintoma: valor}))

def main():
    root = Tk()
    # Pasa enviar_informacion como enviar_callback
    interfaz = InterfazUsuario(root, lambda: enviar_informacion(interfaz))
    root.mainloop()

if __name__ == "__main__":
    main()
