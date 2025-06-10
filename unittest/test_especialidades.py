import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from clases.clinica import Clinica
from clases.medico import Medico
from clases.especialidad import Especialidad
from excepciones.exceptions import *

class TestEspecialidades(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica({}, {}, [], {}) # Clínica modelo
        self.medico = Medico("Dr. Smith", "123456789", [Especialidad("Pediatría", ["Lunes", "Martes"])]) # médico modelo
        self.clinica.agregar_medico(self.medico) # Agregar el médico a la clínica para pruebas

    def test_agregar_especialidad_a_medico(self):
        especialidad = Especialidad("Cardiología", ["Lunes", "Miércoles"]) # nueva especialidad modelo
        self.clinica.agregar_especialidad_a_medico(self.medico.obtener_matricula, especialidad)
        self.assertIn(especialidad, self.medico.__especialidades__) # Verifica que la especialidad se haya agregado correctamente
    
    def test_no_duplicar_especialidad(self):
        especialidad = Especialidad("Pediatría", ["Lunes", "Martes"]) # se crea una especialidad ya existente
        with self.assertRaises(ValueError):
            self.clinica.agregar_especialidad_a_medico(self.medico.obtener_matricula, especialidad) # comprueba que se lance un ValueError al intentar agregar una especialidad duplicada
    
    def test_dia_invalido_en_especialidad(self):
        with self.assertRaises(ValueError):
            Especialidad("Dermatología", ["Lunes", "Vielne"])  # Día inválido
    
    def test_agregar_especialidad_a_medico_no_registrado(self):
        especialidad = Especialidad("Neurología", ["Martes", "Jueves"])
        with self.assertRaises(MedicoNoDisponibleError):
            self.clinica.agregar_especialidad_a_medico("999999999", especialidad)

if __name__ == '__main__':
    unittest.main()