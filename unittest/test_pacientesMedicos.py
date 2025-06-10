import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import datetime
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.especialidad import Especialidad  # Importar la clase Especialidad para usarla en las pruebas

class TestPacientesMedicos(unittest.TestCase):

    # CONFIGURACIÓN INICIAL DE UN MODELO DE CLÍNICA PARA LAS PRUEBAS
    def setUp(self):
        self.clinica = Clinica({}, {}, [], {})

    # PRUEBA DE REGISTRO DE PACIENTES
    def test_registro_paciente(self):
        paciente = Paciente("Juan Pérez", "12345678", datetime.date(1959, 8, 11)) # se crea un paciente modelo
        self.clinica.agregar_paciente(paciente) # se agrega el paciente a la clínica
        self.assertIn(paciente, self.clinica.obtener_pacientes()) # se verifica que el paciente esté registrado
    
    # PRUEBA DE REGISTRO DE MÉDICOS
    def test_registro_medico(self):
        # se crean especialidades modelo
        especialidad1 = Especialidad("Cardiología", ["Lunes", "Miércoles", "Viernes"])
        especialidad2 = Especialidad("Pediatría", ["Martes", "Jueves"])
        # se crea un médico modelo con las especialidades
        medico = Medico('Pepito Honguito','987654321', [especialidad1, especialidad2])
        self.clinica.agregar_medico(medico) #se agrega el médico a la clínica
        self.assertIn(medico, self.clinica.obtener_medicos())
    
    # PRUEBAS DE REGISTRO DUPLICADO
    def test_registro_paciente_duplicado(self):
        paciente = Paciente("Juan Pérez", "12345678", datetime.date(1959, 8, 11))
        self.clinica.agregar_paciente(paciente)
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(paciente)

    def test_registro_medico_duplicado(self):
        especialidad1 = Especialidad("Cardiología", ["Lunes", "Miércoles", "Viernes"]) # especialidad modelo para agregarle al médico
        medico = Medico('Pepito Honguito','987654321', [especialidad1])
        self.clinica.agregar_medico(medico)
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(medico)
    
    # VERIFICACIÓN DE ERRORES POR DATOS FALTANTES O INVÁLIDOS
    def test_registro_paciente_datos_invalidos(self):
        # Errores de tipo
        with self.assertRaises(TypeError):
            self.clinica.agregar_paciente(Paciente(123, "12345678", datetime.date(1959, 8, 11)))
        with self.assertRaises(TypeError):
            self.clinica.agregar_paciente(Paciente("Juan Pérez", 12345678, datetime.date(1959, 8, 11)))
        with self.assertRaises(TypeError):
            self.clinica.agregar_paciente(Paciente("Juan Pérez", "12345678", "1959-08-11"))

        # Errores de valor
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(Paciente("", "12345678", datetime.date(1959, 8, 11)))  # Nombre vacío

        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(Paciente("Juan Pérez", "", datetime.date(1959, 8, 11)))  # DNI vacío

        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(Paciente("Juan Pérez", "12345678", None))  # Fecha de nacimiento nula
    
    def test_registro_medico_datos_invalidos(self):
        # Errores de tipo
        with self.assertRaises(TypeError):
            self.clinica.agregar_medico(Medico(123, "12345678", [Especialidad("Cardiología", ["Lunes"])])) 
        with self.assertRaises(TypeError):
            self.clinica.agregar_medico(Medico("Pepito Honguito", 12345678, [Especialidad("Cardiología", ["Lunes"])]))
        with self.assertRaises(TypeError):
            self.clinica.agregar_medico(Medico("Pepito Honguito", "12345678", "Cardiólogo"))

        # Errores de valor
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(Medico("", "12345678", [Especialidad("Cardiología", ["Lunes"])]))  # Nombre vacío

        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(Medico("Pepito Honguito", "", [Especialidad("Cardiología", ["Lunes"])]))  # Matrícula vacía

        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(Medico("Pepito Honguito", "12345678", []))  # especialidad nula


if __name__ == "__main__":
    unittest.main()  # se ejecutan las pruebas