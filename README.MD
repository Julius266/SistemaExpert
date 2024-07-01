# 🩺 Sistema de Diagnóstico de Enfermedades Basado en Reglas

## 🌟 [Descripción](#descripción)

Este proyecto implementa un sistema de diagnóstico de enfermedades basado en reglas utilizando Python 🐍 y la librería `experta`. A través de una interfaz de usuario sencilla, se recopilan los síntomas del usuario y se proporciona un diagnóstico preliminar basado en un conjunto de reglas predefinidas.

## 🏥 [Reglas de Diagnóstico](#reglas-de-diagnóstico)
- Se utiliza la lógica de Forward Chaining para deducir posibles enfermedades basadas en los síntomas proporcionados.
- Las reglas son definidas para identificar enfermedades comunes como la gripe, faringitis, bronquitis, entre otras.
- El sistema proporciona un diagnóstico preliminar y recomienda la consulta con un profesional de la salud.

## 🧠 [Lógica del Sistema](#lógica-del-sistema)
- **Forward Chaining:** El sistema utiliza una estrategia de encadenamiento hacia adelante para deducir posibles diagnósticos basados en los síntomas proporcionados.
- **Motor de Inferencia:** Se implementa un motor de inferencia para evaluar las reglas y proporcionar diagnósticos.
- **Interfaz de Usuario:** Una interfaz de usuario simple para recopilar la información del usuario y sus síntomas.

## 🌟 [Características](#características)
- **Interfaz Amigable:** 👍 Diseño intuitivo y fácil de usar.
- **Diagnóstico Preliminar:** 📋 Obtén un diagnóstico preliminar basado en los síntomas proporcionados.
- **Recomendaciones de Salud:** 🩺 Recomendaciones para consultar con un profesional de la salud.
- **Pruebas Automatizadas:** 🧪 Verifica la lógica del sistema mediante pruebas automatizadas.

## 💉 [Síntomas y Posibles Enfermedades](#síntomas-y-posibles-enfermedades)

El sistema está diseñado para reconocer una variedad de síntomas comunes y proporcionar diagnósticos preliminares basados en ellos. Algunos de los síntomas que el sistema puede reconocer incluyen:

- Fiebre
- Dolor de garganta
- Dolor de cabeza
- Congestión nasal
- Tos

Basándose en los síntomas proporcionados, el sistema puede sugerir las siguientes posibles enfermedades:

- **Faringitis:** Si se detecta fiebre y dolor de garganta.
- **Gripe:** Si se detecta fiebre y dolor de cabeza.
- **Resfriado Común:** Si se detecta dolor de cabeza y congestión nasal.
- **Bronquitis:** Si se detecta dolor de cabeza y tos.
- **Sinusitis:** Si se detecta congestión nasal y tos.
- **Alergia:** Si se detecta congestión nasal sin fiebre.

Es importante recordar que estos diagnósticos son preliminares y siempre se debe consultar a un profesional de la salud para un diagnóstico adecuado.

## 🔧 [Instalación y Configuración](#instalación-y-configuración)

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/Julius266/SistemaExpert.git
    ```

2. **Cambia al directorio del proyecto:**
    ```bash
    cd SistemaExpert
    ```

3. **Crea un ambiente conda:**
    ```bash
    conda create --name SistemaExpert python=3.x
    ```

4. **Activa el ambiente conda:**
    ```bash
    conda activate SistemaExpert
    ```

5. **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Ejecuta el programa principal:**
    ```bash
    python main.py
    ```

## 🧪 [Pruebas](#pruebas)

Este proyecto incluye una suite de pruebas diseñada para validar la lógica y funcionalidad del sistema de diagnóstico. Para ejecutar las pruebas, puedes utilizar `pytest` o `unittest` como se describe a continuación:

### Usando pytest

1. **Instala pytest si aún no lo has hecho:**
    ```bash
    pip install pytest
    ```

2. **Ejecuta las pruebas con `pytest`:**
    ```bash
    pytest -v -s -l --durations=0 ./tests/test_diagnostico.py
    ```

    Los flags `-v`, `-s`, `-l` y `--durations=0` proporcionan una salida detallada, mostrando todas las pruebas que se ejecutan y el tiempo que tarda cada una.

### Usando unittest

1. **Ejecuta las pruebas con `unittest` para `test_diagnostico.py`:**
    ```bash
    python -m unittest discover tests
    ```

    Esto ejecutará todas las pruebas contenidas en el directorio `tests`.

Ambas herramientas proporcionan una manera efectiva de validar que el código funcione como se espera y ayudan a identificar problemas antes de que lleguen a la producción.

## 🔗 [Enlace del Proyecto](#enlace-del-proyecto)

[Sistema de Diagnóstico de Enfermedades Basado en Reglas](https://github.com/Julius266/SistemaExpert.git)
