import datetime
from paciente import Paciente
from medico import Medico
from turno import Turno
from historiaClinica import HistoriaClinica
from receta import Receta

class Clinica:
    # CONSTRUCTOR 
    def __init__(self, pacientes:dict[str, Paciente], medicos:dict[str, Medico], turnos:list[Turno], historias_clinicas:dict[str, HistoriaClinica]):
        self.__pacientes__ = pacientes
        self.__medicos__ = medicos
        self.__turnos__ = turnos
        self.__historias_clinicas__ = historias_clinicas

    # REGISTRO Y ACCESO 
    def agregar_paciente(self, paciente: Paciente): #registra un paciente y crea su historia clinica
        self.__pacientes__[paciente.obtener_dni] = paciente
        self.__historias_clinicas__[paciente.obtener_dni] = HistoriaClinica(paciente, [], [])
    
    def agregar_medico(self, medico: Medico): #registra un medico
        self.__medicos__[medico.obtener_matricula] = medico
    
    def obtener_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes__.values())
    
    def obtener_medicos(self) -> list[Medico]:
        return list(self.__medicos__.values())
    
    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        return self.__medicos__.get(matricula)
    
    # TURNOS
    def agendar_turno(self, dni:str, matricula:str, especialidad:str, fecha_hora:datetime.datetime):
        paciente = self.__pacientes__.get(dni)
        medico = self.__medicos__.get(matricula)
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos__.append(turno)
        self.__historias_clinicas__[dni].agregar_turno(turno)

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos__
    
    # RECETAS E HISTORIAS CLÍNICAS
    def emitir_receta(self, dni:str, matricula:str, medicamentos:list[str]):
        paciente = self.__pacientes__.get(dni)
        medico = self.__medicos__.get(matricula)
        if not paciente or not medico:
            raise ValueError("Paciente o médico no encontrado")
        receta = Receta(paciente, medico, medicamentos, datetime.date.today())
        historia = self.__historias_clinicas__.get(dni)
        if historia:
            historia.agregar_receta(receta)
        else:
            raise ValueError("No se encontró una historia clínica para el paciente de DNI: " + dni)
        
    def obtener_historia_clinica(self, dni:str) -> HistoriaClinica:
        return self.__historias_clinicas__.get(dni)
    
    # VALIDACIONES Y UTILIDADES: se agregarán cuando se cumpla el issue de crear excepciones.