import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import datetime
import unittest
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.turno import Turno
from clases.especialidad import Especialidad
from excepciones.exceptions import *

class TestTurnos(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica({}, {}, [], {})
        self.paciente = Paciente("Juan Perez", "12345678", datetime.date(1990, 1, 1))
        self.medico = Medico("Dr. Smith", "1234", [Especialidad("Cardiología", ["Lunes", "Miércoles"])])
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
    
    def test_agendar_turno_exitoso(self):
        fecha_hora = datetime.datetime(2025, 6, 25, 10, 0)
        turno = self.clinica.agendar_turno(self.paciente.obtener_dni, self.medico.obtener_matricula, "Cardiología", fecha_hora)
        self.assertIsInstance(turno, Turno)

    def test_agendar_turno_paciente_no_encontrado(self):
        with self.assertRaises(PacienteNoEncontradoError):
            self.clinica.agendar_turno("99999999", self.medico.obtener_matricula, "Cardiología", datetime.datetime(2025, 6, 25, 10, 0))
    
    def test_agendar_turno_medico_no_encontrado(self):
        with self.assertRaises(MedicoNoDisponibleError):
            self.clinica.agendar_turno(self.paciente.obtener_dni, "9999", "Cardiología", datetime.datetime(2025, 6, 25, 10, 0))

    def test_agendar_turno_especialidad_no_disponible(self):
        with self.assertRaises(ValueError):
            self.clinica.agendar_turno(self.paciente.obtener_dni, self.medico.obtener_matricula, "Neurología", datetime.datetime(2025, 6, 25, 10, 0))
    
    # el médico no atiende x día de la semana
    def test_agendar_turno_dia_no_disponible(self):
        with self.assertRaises(ValueError):
            self.clinica.agendar_turno(self.paciente.obtener_dni, self.medico.obtener_matricula, "Cardiología", datetime.datetime(2025, 6, 27, 10, 0))  # Viernes no disponible

if __name__ == '__main__':
    unittest.main()