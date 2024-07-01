"""
Este módulo contiene pruebas unitarias para la clase Diagnostico.
"""
import unittest
from src.diagnostico import Diagnostico, Sintoma

class TestDiagnostico(unittest.TestCase):
    """
    Un conjunto de pruebas unitarias para la clase Diagnostico.
    """
    def setUp(self):
        """
        Configuración inicial antes de cada prueba.
        """
        print("\nIniciando una nueva prueba")
        self.motor_diagnostico = Diagnostico()
        self.diagnostico = None

    def tearDown(self):
        """
        Limpieza después de cada prueba.
        """
        print(f"Diagnóstico obtenido: {self.diagnostico}")
        print("Finalizando la prueba\n")

    def run_diagnostico(self, sintomas):
        """
        Ejecuta el motor de diagnóstico con los síntomas proporcionados.
        """
        self.motor_diagnostico.reset()
        self.motor_diagnostico.declare(Sintoma(**sintomas))
        self.motor_diagnostico.run()
        self.diagnostico = self.motor_diagnostico.obtener_diagnostico()

    def test_faringitis(self):
        """
        Prueba para verificar el diagnóstico de faringitis.
        """
        print("Prueba para verificar el diagnóstico de faringitis")
        self.run_diagnostico({'fiebre': 's', 'dolor_de_garganta': 's'})
        self.assertIn("Posible faringitis" , self.diagnostico)

    def test_gripe(self):
        """
        Prueba para verificar el diagnóstico de gripe.
        """
        print("Prueba para verificar el diagnóstico de gripe")
        self.run_diagnostico({'fiebre': 's', 'dolor_de_garganta': 'n', 'dolor_de_cabeza': 's'})
        self.assertIn("Posible gripe",self.diagnostico)

    def test_resfriado_comun(self):
        """
        Prueba para verificar el diagnóstico de resfriado común.
        """
        print("Prueba para verificar el diagnóstico de resfriado común")
        self.run_diagnostico({'fiebre': 'n', 'dolor_de_cabeza': 's', 'congestion_nasal': 's'})
        self.assertIn("Posible resfriado común",self.diagnostico,)

    def test_bronquitis(self):
        """
        Prueba para verificar el diagnóstico de bronquitis.
        """
        print("Prueba para verificar el diagnóstico de bronquitis")
        self.run_diagnostico({'fiebre': 'n', 'dolor_de_cabeza': 's',
        'congestion_nasal': 'n', 'tos': 's'})
        self.assertIn("Posible bronquitis",self.diagnostico,)

    def test_sinusitis(self):
        """
        Prueba para verificar el diagnóstico de sinusitis.
        """
        print("Prueba para verificar el diagnóstico de sinusitis")
        self.run_diagnostico({'fiebre': 'n', 'dolor_de_cabeza': 'n', 'congestion_nasal': 's',
        'tos': 's'})
        self.assertIn("Posible sinusitis", self.diagnostico)

    def test_alergia(self):
        """
        Prueba para verificar el diagnóstico de alergia.
        """
        print("Prueba para verificar el diagnóstico de alergia")
        self.run_diagnostico({'fiebre': 'n', 'dolor_de_cabeza': 'n', 'congestion_nasal': 's',
        'tos': 'n'})
        self.assertIn("Posible alergia",self.diagnostico)

    def test_sintomas_no_reconocidos(self):
        """
        Prueba para verificar el diagnóstico de síntomas no reconocidos.
        """
        print("Prueba para verificar el diagnóstico de síntomas no reconocidos")
        self.run_diagnostico({'fiebre': 'n', 'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 'n', 'congestion_nasal': 'n', 'tos': 'n'})
        self.assertIn("Síntomas no reconocidos",self.diagnostico)

if __name__ == "__main__":
    unittest.main()
