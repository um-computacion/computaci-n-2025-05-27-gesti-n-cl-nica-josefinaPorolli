'''✅ Confirmar que los turnos y recetas se guardan correctamente en la historia clínica del paciente'''

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import datetime
import unittest
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.turno import Turno
from clases.receta import Receta
from clases.especialidad import Especialidad
from clases.historiaClinica import HistoriaClinica
from excepciones.exceptions import *

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para los tests
        self.clinica = Clinica({}, {}, [], {})
        self.paciente = Paciente("Juan Perez", "12345678", datetime.date(1990, 1, 1))
        self.medico = Medico("Dr. Smith", "1234", [Especialidad("Cardiología", ["Lunes", "Miércoles"])])
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_turno_en_historia_clinica(self): # Confirmar que los turnos se guardan en la historia clínica
        fecha_hora = datetime.datetime(2025, 6, 25, 10, 0)
        turno = self.clinica.agendar_turno(self.paciente.obtener_dni, self.medico.obtener_matricula, "Cardiología", fecha_hora) # crear un turno. agendar turno involucra agendarlo en la historia clínica  
        
        historia_clinica = self.clinica.__historias_clinicas__[self.paciente.obtener_dni] # acceder a la historia clínica del paciente
        self.assertIn(turno, historia_clinica.obtener_turnos) # veridica que el turno se haya guardado en la historia clínica del paciente
    
    def test_receta_en_historia_clinica(self): # Confirma que las recetas se guardan en la historia clinica
        receta = self.clinica.emitir_receta(self.paciente.obtener_dni, self.medico.obtener_matricula, ["Aspirina", "Paracetamol"])
        historia_clinica = self.clinica.__historias_clinicas__[self.paciente.obtener_dni]
        self.assertIn(receta, historia_clinica.obtener_recetas) # verifica que la receta se haya guardado en la historia clínica del paciente

if __name__ == '__main__':
    unittest.main()