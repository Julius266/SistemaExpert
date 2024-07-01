from os import getenv, environ
from dotenv import load_dotenv
import sys

def cargar_variable_entorno(variable):
    valor = getenv(variable)
    if valor is None:
        sys.exit(f"Error: La variable de entorno {variable} no está definida. Asegúrate de haberla definido en el archivo .env")
    return valor

def cargar_variables_entorno():
    load_dotenv()
