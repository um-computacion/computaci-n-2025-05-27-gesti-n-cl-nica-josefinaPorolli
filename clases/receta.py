import datetime
from paciente import Paciente
from medico import Medico
class Receta:
    # CONSTRUCTOR
    def __init__(self, paciente:Paciente, medico:Medico, medicamentos:list[str], fecha:datetime.date):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha__ = fecha
    
    # REPRESENTACION
    def __str__(self) -> str:
        medicamentos_str = ', '.join(self.__medicamentos__)
        return (f"RECETA\nFecha: {self.__fecha__}\nPaciente: {self.__paciente__.obtener_nombre}\nMedico: {self.__medico__.obtener_nombre}\nMedicamentos: {medicamentos_str}")