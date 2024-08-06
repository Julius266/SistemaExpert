import os
from dotenv import load_dotenv
from tkinter import Tk, PhotoImage, messagebox
import tkinter as tk
from src.utils.helpers import cargar_variable_entorno
from src.diagnostico import Diagnostico, Sintoma

class InterfazUsuario:
    def __init__(self, root, enviar_callback):
        self.root = root
        self.root.title("Información del Usuario")
        self.root.geometry("1000x800")
        self.root.configure(bg='#e6f7ff')  # Fondo azul claro

        # Estilo y fuentes
        self.title_font = ("Helvetica Neue", 24, "bold")
        self.label_font = ("Helvetica Neue", 14)
        self.button_font = ("Helvetica Neue", 14, "bold")

        # Agregar imagen de Dr. Simi
        image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'dr-simi.png')
        self.simi_image = PhotoImage(file=image_path)
        self.simi_label = tk.Label(root, image=self.simi_image, bg='#e6f7ff')
        self.simi_label.pack(pady=20)

        # Título
        self.title_label = tk.Label(root, text="Sistema Experto de Diagnóstico", font=self.title_font, bg='#e6f7ff')
        self.title_label.pack(pady=10)

        # Nombre
        self.nombre_label = tk.Label(root, text="Por favor, ingresa tu nombre:", font=self.label_font, bg='#e6f7ff')
        self.nombre_label.pack(pady=5)
        self.nombre_entry = tk.Entry(root, font=self.label_font, width=30)
        self.nombre_entry.pack(pady=5)

        # Lugar de origen
        self.lugar_label = tk.Label(root, text="Ingresa tu lugar de origen:", font=self.label_font, bg='#e6f7ff')
        self.lugar_label.pack(pady=5)
        self.lugar_entry = tk.Entry(root, font=self.label_font, width=30)
        self.lugar_entry.pack(pady=5)

        # Botón para ingresar síntomas
        self.sintomas_button = tk.Button(root, text="Ingresar síntomas", font=self.button_font, command=self.obtener_sintomas_usuario, bg='#007acc', fg='white', relief=tk.FLAT)
        self.sintomas_button.pack(pady=20)

        # Botón para enviar información
        self.enviar_button = tk.Button(root, text="Enviar", font=self.button_font, command=enviar_callback, bg='#007acc', fg='white', relief=tk.FLAT)
        self.enviar_button.pack(pady=10)

        self.sintomas_usuario = {}

    def obtener_informacion_usuario(self):
        nombre = self.nombre_entry.get()
        lugar = self.lugar_entry.get()
        return {"nombre": nombre, "lugar": lugar}

    def obtener_sintomas_usuario(self):
        self.sintomas_window = tk.Toplevel(self.root)
        self.sintomas_window.title("Síntomas del Usuario")
        self.sintomas_window.geometry("400x600")  # Ajusta el tamaño de la ventana aquí
        self.sintomas_window.configure(bg='#e6f7ff')

        ruta_sintomas = cargar_variable_entorno('SINTOMAS_FILE_PATH')
        try:
            with open(ruta_sintomas, 'r', encoding='utf-8') as file:
                sintomas = [line.strip().replace('_', ' ') for line in file.readlines()]  # Reemplaza los guiones bajos por espacios
                for sintoma in sintomas:
                    var = tk.StringVar(value='n')
                    frame = tk.Frame(self.sintomas_window, pady=5, bg='#e6f7ff')
                    frame.pack(anchor="w")
                    label = tk.Label(frame, text=f"Tiene {sintoma}?", font=self.label_font, bg='#e6f7ff')
                    label.pack(side=tk.LEFT, padx=5)
                    si_radio = tk.Radiobutton(frame, text="Sí", variable=var, value='s', font=self.label_font, bg='#e6f7ff')
                    si_radio.pack(side=tk.LEFT, padx=5)
                    no_radio = tk.Radiobutton(frame, text="No", variable=var, value='n', font=self.label_font, bg='#e6f7ff')
                    no_radio.pack(side=tk.LEFT, padx=5)
                    self.sintomas_usuario[sintoma.replace(' ', '_')] = var
        except FileNotFoundError:
            self.mostrar_error(f"El archivo en '{ruta_sintomas}' no se encontró.")
        
        cerrar_button = tk.Button(self.sintomas_window, text="Cerrar", font=self.button_font, command=self.sintomas_window.destroy, bg='#007acc', fg='white', relief=tk.FLAT)
        cerrar_button.pack(pady=20)

    def obtener_sintomas(self):
        return {k: v.get() for k, v in self.sintomas_usuario.items()}

    def imprimir_resultados(self, usuario, diagnostico):
        resultado = f"{usuario['nombre']}, basado en tus síntomas:\n"
        if diagnostico:
            if isinstance(diagnostico, list):
                for diag in diagnostico:
                    resultado += "- " + diag + "\n"
            else:
                resultado += "- " + diagnostico + "\n"
        else:
            resultado += "No se pudo determinar un diagnóstico basado en los síntomas proporcionados.\n"
        
        # Crear una nueva ventana para mostrar los resultados con la imagen
        self.resultado_window = tk.Toplevel(self.root)
        self.resultado_window.title("Resultados del Diagnóstico")
        self.resultado_window.geometry("1000x600")  # Ajusta la altura de la ventana aquí
        self.resultado_window.configure(bg='#e6f7ff')

        # Agregar la imagen de Diagnostico a la ventana de resultados
        image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'diagnostico.png')
        self.simi_image_resultado = PhotoImage(file=image_path)
        self.simi_image_resultado = self.simi_image_resultado.subsample(2)
        self.simi_label_resultado = tk.Label(self.resultado_window, image=self.simi_image_resultado, bg='#e6f7ff')
        self.simi_label_resultado.pack(pady=20)

        # Agregar el texto del resultado centrado a la ventana de resultados
        self.resultado_label = tk.Label(self.resultado_window, text=resultado, font=self.label_font, bg='#e6f7ff', justify=tk.CENTER, wraplength=900)
        self.resultado_label.pack(fill=tk.BOTH, expand=True)

        # Agregar el texto de advertencia en letras pequeñas
        self.advertencia_label = tk.Label(self.resultado_window, text=(
            "Recuerda, los diagnósticos proporcionados son solamente posibilidades y no deben ser "
            "considerados como diagnósticos médicos definitivos. Por favor, consulta a un profesional "
            "de la salud para obtener un diagnóstico adecuado."
        ), font=("Helvetica Neue", 10), bg='#e6f7ff', justify=tk.CENTER, wraplength=900)
        self.advertencia_label.pack(pady=10)

        cerrar_button = tk.Button(self.resultado_window, text="Cerrar", font=self.button_font, command=self.resultado_window.destroy, bg='#007acc', fg='white', relief=tk.FLAT)
        cerrar_button.pack(pady=20)

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

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
    load_dotenv()
    main()
