import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import datetime
import unittest
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.receta import Receta
from clases.especialidad import Especialidad
from excepciones.exceptions import *

class TestRecetas(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica({}, {}, [], {})
        self.paciente = Paciente("Juan Perez", "12345678", datetime.date(1990, 1, 1))
        self.medico = Medico("Dr. Smith", "1234", [Especialidad("Cardiología", ["Lunes", "Miércoles"])])
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
    
    def test_receta_exitosa(self):
        receta = Receta(self.paciente.obtener_dni, self.medico.obtener_matricula, ["Aspirina", "Paracetamol"])
        self.clinica.__historias_clinicas__[self.paciente.obtener_dni].agregar_receta(receta)
        self.assertIn(receta, self.clinica.__historias_clinicas__[self.paciente.obtener_dni].obtener_recetas)

    def test_receta_exitosa(self):
        receta = Receta(self.paciente, self.medico, ["Aspirina", "Paracetamol"])
        self.clinica.__historias_clinicas__[self.paciente.obtener_dni].agregar_receta(receta)
        self.assertIn(receta, self.clinica.__historias_clinicas__[self.paciente.obtener_dni].obtener_recetas)
    
    def test_receta_medico_no_encontrado(self):
        with self.assertRaises(MedicoNoDisponibleError):
            self.clinica.emitir_receta(self.paciente.obtener_dni, "9999", ["Aspirina", "Paracetamol"])
    
    def test_receta_paciente_no_encontrado(self):
        with self.assertRaises(PacienteNoEncontradoError):
            self.clinica.emitir_receta("99999", self.medico.obtener_matricula, ["Aspirina", "Paracetamol"])

    def test_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaError):
            self.clinica.emitir_receta(self.paciente.obtener_dni, self.medico.obtener_matricula, [])

if __name__ == '__main__':
    unittest.main()