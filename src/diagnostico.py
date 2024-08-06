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
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Faringitis: Inflamación de la garganta causada por infección o irritación."))

    @Rule(EstadoDiagnostico(nombre="posible_fiebre_detectada"),
          AND(Sintoma(dolor_de_garganta='n'), Sintoma(dolor_de_cabeza='s')))
    def regla3(self):
        """Si se ha detectado posible fiebre, no hay dolor de garganta pero hay dolor de cabeza,
        se sugiere posible gripe."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Gripe: Infección viral que afecta las vías respiratorias."))

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fiebre='n'), Sintoma(dolor_de_cabeza='s')))
    def regla4(self):
        """Si el estado es inicial, no hay fiebre pero hay dolor de cabeza,
        se declara posible dolor de cabeza detectado."""
        self.declare(EstadoDiagnostico(nombre="posible_dolor_cabeza_detectado", diagnostico="indefinido"))

    @Rule(EstadoDiagnostico(nombre="posible_dolor_cabeza_detectado"), AND(Sintoma(congestion_nasal='s')))
    def regla5(self):
        """Si se ha detectado posible dolor de cabeza y hay congestión nasal,
        se sugiere posible resfriado común."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Resfriado común: Infección viral leve que afecta las vías respiratorias superiores."))

    @Rule(EstadoDiagnostico(nombre="posible_dolor_cabeza_detectado"),
          AND(Sintoma(congestion_nasal='n'), Sintoma(tos='s')))
    def regla6(self):
        """Si se ha detectado posible dolor de cabeza, no hay congestión nasal pero hay tos,
        se sugiere posible bronquitis."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Bronquitis: Inflamación de los bronquios en los pulmones."))

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fiebre='n'), Sintoma(dolor_de_cabeza='n'), Sintoma(congestion_nasal='s')))
    def regla7(self):
        """Si el estado es inicial, no hay fiebre, no hay dolor de cabeza pero hay congestión nasal,
        se declara posible congestión detectada."""
        self.declare(EstadoDiagnostico(nombre="posible_congestion_detectada", diagnostico="indefinido"))

    @Rule(EstadoDiagnostico(nombre="posible_congestion_detectada"), AND(Sintoma(tos='s')))
    def regla8(self):
        """Si se ha detectado posible congestión y hay tos, se sugiere posible sinusitis."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Sinusitis: Inflamación de los senos paranasales."))

    @Rule(EstadoDiagnostico(nombre="posible_congestion_detectada"), AND(Sintoma(tos='n')))
    def regla9(self):
        """Si se ha detectado posible congestión y no hay tos, se sugiere posible alergia."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Alergia: Reacción del sistema inmunológico a sustancias externas."))

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(nauseas='s'), Sintoma(dolor_abdominal='s')))
    def regla11(self):
        """Si hay nauseas y dolor abdominal, posible intoxicación alimentaria."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Intoxicación alimentaria: Enfermedad causada por ingerir alimentos contaminados."))

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(diarrea='s'), Sintoma(fiebre='s')))
    def regla12(self):
        """Si hay diarrea y fiebre, posible infección gastrointestinal."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Infección gastrointestinal: Infección del sistema digestivo por bacterias o virus."))

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fatiga='s'), Sintoma(dolor_muscular='s')))
    def regla13(self):
        """Si hay fatiga y dolor muscular, posible infección viral."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Infección viral: Infección causada por virus, puede afectar diferentes partes del cuerpo."))

    @Rule(EstadoDiagnostico(nombre="inicial"))
    def regla10(self):
        """Si el estado es inicial y no se cumplen otras condiciones,
        se declara que los síntomas no son reconocidos."""
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="No existen síntomas para diagnosticar una enfermedad."))

    def obtener_diagnostico(self, sintomas):
        """Obtiene el diagnóstico basado en los hechos y reglas definidas.

        Args:
            sintomas (dict): Diccionario con los síntomas del usuario.

        Returns:
            str: El diagnóstico resultante o un mensaje indicando que no se encontró diagnóstico.
        """
        if not sintomas:
            return "No se proporcionaron suficientes síntomas para un diagnóstico."

        if len([v for v in sintomas.values() if v == 's']) == 1:
            return "No hay suficientes síntomas para dar un diagnóstico adecuado."

        diagnosticos = []
        for i in range(len(self.facts)):
            hecho = self.facts[i].as_dict()
            if hecho.get('nombre') == 'final' and hecho.get('diagnostico') != "No existen síntomas para diagnosticar una enfermedad.":
                diagnosticos.append(hecho.get('diagnostico'))

        if len(diagnosticos) == 0:
            return "No se pudo determinar un diagnóstico basado en los síntomas proporcionados."

        return ', '.join(diagnosticos)
