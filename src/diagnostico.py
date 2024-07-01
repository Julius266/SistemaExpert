"""
Este módulo define un sistema experto para diagnosticar enfermedades basado en síntomas
utilizando la biblioteca Experta.

Classes:
    Sintoma: Representa un síntoma que puede presentar un paciente.
    EstadoDiagnostico: Representa el estado actual del diagnóstico.
    Diagnostico: Motor de conocimiento que contiene las reglas y hechos
    para realizar el diagnóstico.

Usage:
    Crear una instancia de la clase Diagnostico y utilizar el método obtener_diagnostico para
    obtener un diagnóstico basado en los síntomas proporcionados.
"""

from experta import KnowledgeEngine, Fact, Rule, AND, DefFacts

class Sintoma(Fact):
    """Representa un síntoma que puede presentar un paciente."""

class EstadoDiagnostico(Fact):
    """Representa el estado actual del diagnóstico."""

class Diagnostico(KnowledgeEngine):
    """Motor de conocimiento que contiene las reglas y hechos para realizar el diagnóstico."""
    @DefFacts()
    def _initial_facts(self):
        """Define los hechos iniciales del motor de conocimiento."""
        yield EstadoDiagnostico(nombre="inicial", diagnostico="indefinido")

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fiebre='s')))
    def regla1(self):
        """Si el estado es inicial y hay fiebre, posible fiebre detectada."""
        self.declare(EstadoDiagnostico(nombre="posible_fiebre_detectada", diagnostico="indefinido"))

    @Rule(EstadoDiagnostico(nombre="posible_fiebre_detectada"), AND(Sintoma(dolor_de_garganta='s')))
    def regla2(self):
        """Si se ha detectado posible fiebre y hay dolor de garganta, se sugiere posible faringitis."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible faringitis"))

    @Rule(EstadoDiagnostico(nombre="posible_fiebre_detectada"),
          AND(Sintoma(dolor_de_garganta='n'), Sintoma(dolor_de_cabeza='s')))
    def regla3(self):
        """Si se ha detectado posible fiebre, no hay dolor de garganta pero hay dolor de cabeza,
        se sugiere posible gripe."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible gripe"))

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fiebre='n'), Sintoma(dolor_de_cabeza='s')))
    def regla4(self):
        """Si el estado es inicial, no hay fiebre pero hay dolor de cabeza,
        se declara posible dolor de cabeza detectado."""
        self.declare(EstadoDiagnostico(nombre="posible_dolor_cabeza_detectado", diagnostico="indefinido"))

    @Rule(EstadoDiagnostico(nombre="posible_dolor_cabeza_detectado"), AND(Sintoma(congestion_nasal='s')))
    def regla5(self):
        """Si se ha detectado posible dolor de cabeza y hay congestión nasal,
        se sugiere posible resfriado común."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible resfriado común"))

    @Rule(EstadoDiagnostico(nombre="posible_dolor_cabeza_detectado"),
          AND(Sintoma(congestion_nasal='n'), Sintoma(tos='s')))
    def regla6(self):
        """Si se ha detectado posible dolor de cabeza, no hay congestión nasal pero hay tos,
        se sugiere posible bronquitis."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible bronquitis"))

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fiebre='n'), Sintoma(dolor_de_cabeza='n'), Sintoma(congestion_nasal='s')))
    def regla7(self):
        """Si el estado es inicial, no hay fiebre, no hay dolor de cabeza pero hay congestión nasal,
        se declara posible congestión detectada."""
        self.declare(EstadoDiagnostico(nombre="posible_congestion_detectada", diagnostico="indefinido"))

    @Rule(EstadoDiagnostico(nombre="posible_congestion_detectada"), AND(Sintoma(tos='s')))
    def regla8(self):
        """Si se ha detectado posible congestión y hay tos, se sugiere posible sinusitis."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible sinusitis"))

    @Rule(EstadoDiagnostico(nombre="posible_congestion_detectada"), AND(Sintoma(tos='n')))
    def regla9(self):
        """Si se ha detectado posible congestión y no hay tos, se sugiere posible alergia."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible alergia"))

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(nauseas='s'), Sintoma(dolor_abdominal='s')))
    def regla11(self):
        """Si hay nauseas y dolor abdominal, posible intoxicación alimentaria."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible intoxicación alimentaria"))

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(diarrea='s'), Sintoma(fiebre='s')))
    def regla12(self):
        """Si hay diarrea y fiebre, posible infección gastrointestinal."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible infección gastrointestinal"))

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fatiga='s'), Sintoma(dolor_muscular='s')))
    def regla13(self):
        """Si hay fatiga y dolor muscular, posible infección viral."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible infección viral"))

    @Rule(EstadoDiagnostico(nombre="inicial"))
    def regla10(self):
        """Si el estado es inicial y no se cumplen otras condiciones,
        se declara que los síntomas no son reconocidos."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="No existen síntomas para diagnosticar una enfermedad."))

    def obtener_diagnostico(self):
        """Obtiene el diagnóstico basado en los hechos y reglas definidas.

        Returns:
            str: El diagnóstico resultante o un mensaje indicando que no se encontró diagnóstico.
        """
        diagnosticos = []
        for i in range(len(self.facts)):
            hecho = self.facts[i].as_dict()
            if hecho.get('nombre') == 'final':
                diagnosticos.append(hecho.get('diagnostico'))
            elif hecho.get('diagnostico') == 'indefinido' and hecho.get('nombre') != 'inicial':
                diagnosticos.append(hecho.get('nombre'))
        if len(diagnosticos) > 1:
            return ', '.join(diagnosticos[:-1])
        if len(diagnosticos) == 1:
            return diagnosticos[0]

        return "Diagnóstico no encontrado"
