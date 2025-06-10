import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import datetime
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico

class TestPacientesMedicos(unittest.TestCase):

    # CONFIGURACIÓN INICIAL DE UN MODELO DE CLÍNICA PARA LAS PRUEBAS
    def setUp(self):
        self.clinica = Clinica({}, {}, [], {})

    # PRUEBA DE REGISTRO DE PACIENTES
    def test_registro_paciente(self):
        paciente = Paciente("Juan Pérez", "12345678", datetime.date(1959, 8, 11)) # se crea un paciente modelo
        self.clinica.agregar_paciente(paciente) # se agrega el paciente a la clínica
        self.assertIn("12345678", self.clinica.obtener_pacientes()) # se verifica que el paciente esté registrado

if __name__ == "__main__":
    unittest.main()  # se ejecutan las pruebas