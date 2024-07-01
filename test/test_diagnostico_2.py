"""
Este módulo contiene pruebas unitarias para la clase Diagnostico.
"""
import pytest
from src.diagnostico import Diagnostico, Sintoma

@pytest.fixture
def motor_diagnostico():
    """
    Fixture de pytest para crear y restablecer un objeto Diagnostico antes de cada prueba.
    """
    motor = Diagnostico()
    motor.reset()
    return motor

# pylint: disable=redefined-outer-name
def test_posible_faringitis(motor_diagnostico):
    """
    Prueba para verificar el diagnóstico de faringitis.
    """
    sintomas = {
        'fiebre': 's',
        'dolor_de_garganta': 's',
        'dolor_de_cabeza': 'n',
        'congestion_nasal': 'n',
        'tos': 'n'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible faringitis" in motor_diagnostico.obtener_diagnostico()

def test_posible_gripe(motor_diagnostico):
    """
    Prueba para verificar el diagnóstico de gripe.
    """
    sintomas = {
        'fiebre': 's',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 's',
        'congestion_nasal': 'n',
        'tos': 'n'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible gripe" in motor_diagnostico.obtener_diagnostico()

def test_posible_resfriado_comun(motor_diagnostico):
    """
    Prueba para verificar el diagnóstico de resfriado común.
    """
    sintomas = {
        'fiebre': 'n',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 's',
        'congestion_nasal': 's',
        'tos': 'n'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible resfriado común" in motor_diagnostico.obtener_diagnostico()

def test_posible_bronquitis(motor_diagnostico):
    """
    Prueba para verificar el diagnóstico de bronquitis.
    """
    sintomas = {
        'fiebre': 'n',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 's',
        'congestion_nasal': 'n',
        'tos': 's'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible bronquitis" in motor_diagnostico.obtener_diagnostico()

def test_posible_sinusitis(motor_diagnostico):
    """
    Prueba para verificar el diagnóstico de sinusitis.
    """
    sintomas = {
        'fiebre': 'n',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 'n',
        'congestion_nasal': 's',
        'tos': 's'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible sinusitis" in motor_diagnostico.obtener_diagnostico()

def test_posible_alergia(motor_diagnostico):
    """
    Prueba para verificar el diagnóstico de alergia.
    """
    sintomas = {
        'fiebre': 'n',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 'n',
        'congestion_nasal': 's',
        'tos': 'n'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible alergia" in motor_diagnostico.obtener_diagnostico()

def test_sintomas_no_reconocidos(motor_diagnostico):
    """
    Prueba para verificar el Síntomas no reconocidos
    """
    sintomas = {
        'fiebre': 'n',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 'n',
        'congestion_nasal': 'n',
        'tos': 'n'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert  motor_diagnostico.obtener_diagnostico()

def test_diagnostico_no_encontrado(motor_diagnostico):
    """
    Prueba para verificar el Síntomas no reconocidos.
    """
    motor_diagnostico.run()
    assert "Síntomas no reconocidos" in motor_diagnostico.obtener_diagnostico()
