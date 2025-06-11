import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import datetime
from .paciente import Paciente
from .medico import Medico
class Receta:
    # CONSTRUCTOR
    def __init__(self, paciente:Paciente, medico:Medico, medicamentos:list[str], fecha:datetime.date = None):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha__ = fecha if fecha else datetime.date.today()  # Si no se proporciona fecha, se usa la fecha actual
    
    # REPRESENTACION
    def __str__(self) -> str:
        medicamentos_str = ', '.join(self.__medicamentos__)
        return (f"RECETA\nFecha: {self.__fecha__}\nPaciente: {self.__paciente__.obtener_nombre} DNI: {self.__paciente__.obtener_dni}\nMedico: {self.__medico__.obtener_nombre} MATRÍCULA: {self.__medico__.obtener_matricula}\nMedicamentos: {medicamentos_str}")