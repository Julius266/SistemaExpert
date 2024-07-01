import tkinter as tk
from tkinter import messagebox, PhotoImage
from src.utils.helpers import cargar_variable_entorno
import os

class InterfazUsuario:
    def __init__(self, root, enviar_callback):
        self.root = root
        self.root.title("Información del Usuario")
        self.root.geometry("800x600")
        self.root.configure(bg='light gray')

        # Estilo y fuentes
        self.title_font = ("Helvetica", 18, "bold")
        self.label_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 12, "bold")

        # Agregar imagen de Dr. Simi
        image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'dr-simi.png')
        self.simi_image = PhotoImage(file=image_path)
        self.simi_label = tk.Label(root, image=self.simi_image, bg='light gray')
        self.simi_label.pack(pady=20)

        # Título
        self.title_label = tk.Label(root, text="Sistema Experto de Diagnóstico", font=self.title_font, bg='light gray')
        self.title_label.pack(pady=10)

        # Nombre
        self.nombre_label = tk.Label(root, text="Por favor, ingresa tu nombre:", font=self.label_font, bg='light gray')
        self.nombre_label.pack(pady=5)
        self.nombre_entry = tk.Entry(root, font=self.label_font, width=30)
        self.nombre_entry.pack(pady=5)

        # Lugar de origen
        self.lugar_label = tk.Label(root, text="Ingresa tu lugar de origen:", font=self.label_font, bg='light gray')
        self.lugar_label.pack(pady=5)
        self.lugar_entry = tk.Entry(root, font=self.label_font, width=30)
        self.lugar_entry.pack(pady=5)

        # Botón para ingresar síntomas
        self.sintomas_button = tk.Button(root, text="Ingresar síntomas", font=self.button_font, command=self.obtener_sintomas_usuario, bg='gray', fg='white')
        self.sintomas_button.pack(pady=20)

        # Botón para enviar información
        self.enviar_button = tk.Button(root, text="Enviar", font=self.button_font, command=enviar_callback, bg='gray', fg='white')
        self.enviar_button.pack(pady=10)

        self.sintomas_usuario = {}

    def obtener_informacion_usuario(self):
        nombre = self.nombre_entry.get()
        lugar = self.lugar_entry.get()
        return {"nombre": nombre, "lugar": lugar}

    def obtener_sintomas_usuario(self):
        self.sintomas_window = tk.Toplevel(self.root)
        self.sintomas_window.title("Síntomas del Usuario")
        self.sintomas_window.geometry("400x400")
        self.sintomas_window.configure(bg='light gray')

        ruta_sintomas = cargar_variable_entorno('SINTOMAS_FILE_PATH')
        try:
            with open(ruta_sintomas, 'r', encoding='utf-8') as file:
                sintomas = [line.strip() for line in file.readlines()]
                for sintoma in sintomas:
                    var = tk.StringVar(value='n')
                    frame = tk.Frame(self.sintomas_window, pady=5, bg='light gray')
                    frame.pack(anchor="w")
                    label = tk.Label(frame, text=f"Tiene {sintoma}?", font=self.label_font, bg='light gray')
                    label.pack(side=tk.LEFT, padx=5)
                    si_radio = tk.Radiobutton(frame, text="Sí", variable=var, value='s', font=self.label_font, bg='light gray')
                    si_radio.pack(side=tk.LEFT, padx=5)
                    no_radio = tk.Radiobutton(frame, text="No", variable=var, value='n', font=self.label_font, bg='light gray')
                    no_radio.pack(side=tk.LEFT, padx=5)
                    self.sintomas_usuario[sintoma] = var
        except FileNotFoundError:
            messagebox.showerror("Error", f"El archivo en '{ruta_sintomas}' no se encontró.")
        
        cerrar_button = tk.Button(self.sintomas_window, text="Cerrar", font=self.button_font, command=self.sintomas_window.destroy, bg='gray', fg='white')
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
        resultado += (
            "Recuerda, los diagnósticos proporcionados son solamente posibilidades y no deben ser "
            "considerados como diagnósticos médicos definitivos. Por favor, consulta a un profesional "
            "de la salud para obtener un diagnóstico adecuado."
        )
        
        # Crear una nueva ventana para mostrar los resultados con la imagen
        self.resultado_window = tk.Toplevel(self.root)
        self.resultado_window.title("Resultados del Diagnóstico")
        self.resultado_window.geometry("600x400")
        self.resultado_window.configure(bg='light gray')

        # Agregar la imagen de Dr. Simi a la ventana de resultados
        image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'dr-simi.png')
        self.simi_image_resultado = PhotoImage(file=image_path)
        self.simi_label_resultado = tk.Label(self.resultado_window, image=self.simi_image_resultado, bg='light gray')
        self.simi_label_resultado.pack(pady=20)

        # Agregar el texto del resultado a la ventana de resultados
        self.resultado_label = tk.Label(self.resultado_window, text=resultado, font=self.label_font, bg='light gray', justify=tk.LEFT)
        self.resultado_label.pack(pady=10)

        cerrar_button = tk.Button(self.resultado_window, text="Cerrar", font=self.button_font, command=self.resultado_window.destroy, bg='gray', fg='white')
        cerrar_button.pack(pady=20)

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    def enviar_informacion(interfaz):
        info_usuario = interfaz.obtener_informacion_usuario()
        sintomas_usuario = interfaz.obtener_sintomas()
        print("Información del usuario:", info_usuario)
        print("Síntomas del usuario:", sintomas_usuario)
        interfaz.imprimir_resultados(info_usuario, "Diagnóstico de prueba")
    
    interfaz = InterfazUsuario(root, lambda: enviar_informacion(interfaz))
    root.mainloop()
