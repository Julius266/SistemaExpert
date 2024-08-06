import os
from dotenv import load_dotenv
from tkinter import Tk
from src.interfaz_usuario import InterfazUsuario
from src.diagnostico import Diagnostico, Sintoma

# Cargar las variables de entorno desde .env
load_dotenv()

def enviar_informacion(interfaz):
    usuario = interfaz.obtener_informacion_usuario()
    
    # Validar que nombre y lugar de origen no estén vacíos
    if not usuario["nombre"] or not usuario["lugar"]:
        messagebox.showerror("Error", "Por favor, ingrese su nombre y lugar de origen antes de enviar los síntomas.")
        return

    sintomas = interfaz.obtener_sintomas()

    try:
        motor_diagnostico = Diagnostico()
        motor_diagnostico.reset()
        declarar_sintomas(motor_diagnostico, sintomas)
        motor_diagnostico.run()
        diagnostico = motor_diagnostico.obtener_diagnostico(sintomas)
        interfaz.imprimir_resultados(usuario, diagnostico)
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

def declarar_sintomas(motor_diagnostico, sintomas):
    for sintoma, valor in sintomas.items():
        motor_diagnostico.declare(Sintoma(**{sintoma: valor}))

def main():
    root = Tk()
    # Pasa enviar_informacion como enviar_callback
    interfaz = InterfazUsuario(root, lambda: enviar_informacion(interfaz))
    root.mainloop()

if __name__ == "__main__":
    load_dotenv()
    main()
