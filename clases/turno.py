import datetime
from paciente import Paciente
from medico import Medico
from especialidad import Especialidad

class Turno:
    # CONSTRUCTOR
    def __init__(self, paciente:Paciente, medico:Medico, fecha_hora:datetime.datetime, especialidad:str):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora
        self.__especialidad__ = especialidad
    
    # GETTERS
    @property
    def obtener_medico(self) -> Medico:
        return self.__medico__
    
    @property
    def obtener_fecha_hora(self) -> datetime.datetime:
        return self.__fecha_hora__
    
    # REPRESENTACION
    def __str__(self) -> str:
        return f"TURNO\nFecha y hora: {self.__fecha_hora__}\nPaciente: {self.__paciente__.obtener_nombre}, DNI: {self.__paciente__.obtener_dni}\nMedico: {self.__medico__.obtener_nombre}, Matrícula: {self.__medico__.obtener_matricula}\nEspecialidad: {self.__especialidad__}" # No se toma solo el dni y la matrícula para que sea más legible para el usuario
    