import datetime
from paciente import Paciente
from medico import Medico
from especialidad import Especialidad

class Turno:
    # CONSTRUCTOR
    def __init__(self, paciente:Paciente, medico:Medico, fecha_hora:datetime.datetime, especialidad:Especialidad):
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
        return f"TURNO\nFecha y hora: {self.__fecha_hora__}\nPaciente: {self.__paciente__.obtener_nombre}\nMedico: {self.__medico__.obtener_nombre}\nEspecialidad: {self.__especialidad__.obtener_nombre}"
    