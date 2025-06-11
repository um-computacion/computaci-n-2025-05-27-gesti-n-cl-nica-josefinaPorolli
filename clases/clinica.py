import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import datetime
from .paciente import Paciente
from .medico import Medico
from .turno import Turno
from .historiaClinica import HistoriaClinica
from .receta import Receta
from .especialidad import Especialidad
from excepciones.exceptions import PacienteNoEncontradoError, MedicoNoDisponibleError, TurnoOcupadoError, RecetaInvalidaError

class Clinica:
    # CONSTRUCTOR 
    def __init__(self, pacientes:dict[str, Paciente], medicos:dict[str, Medico], turnos:list[Turno], historias_clinicas:dict[str, HistoriaClinica]):
        self.__pacientes__ = pacientes
        self.__medicos__ = medicos
        self.__turnos__ = turnos
        self.__historias_clinicas__ = historias_clinicas

    # REGISTRO Y ACCESO 
    def agregar_paciente(self, paciente: Paciente): #registra un paciente y crea su historia clinica
        dni = paciente.obtener_dni
        if dni in self.__pacientes__:
            raise ValueError(f"El paciente con DNI {dni} ya está registrado.")
        self.__pacientes__[dni] = paciente
        self.__historias_clinicas__[dni] = HistoriaClinica(paciente, [], []) # corrección para que lance la excepción
    
    def agregar_medico(self, medico: Medico): #registra un medico
        matricula = medico.obtener_matricula
        if matricula in self.__medicos__:
            raise ValueError(f"El médico con matrícula {matricula} ya está registrado.")
        self.__medicos__[matricula] = medico
    
    def agregar_especialidad_a_medico(self, matricula:str, especialidad:Especialidad):
        # Verificar que el médico esté registrado
        if matricula not in self.__medicos__:
            self.validar_existencia_medico(matricula)

        medico = self.__medicos__[matricula]
        medico.agregar_especialidad(especialidad)
    
    def obtener_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes__.values()) # corrección: se toman los índices de los pacientes
    
    def obtener_medicos(self) -> list[Medico]:
        return list(self.__medicos__.values()) # corrección: se toman los índices de los médicos
    
    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        return self.__medicos__.get(matricula)
    
    # TURNOS
    def agendar_turno(self, dni:str, matricula:str, especialidad:str, fecha_hora:datetime.datetime):
        paciente = self.__pacientes__.get(dni)
        medico = self.__medicos__.get(matricula)
        # Validar existencia de paciente y médico
        if not paciente:
            raise PacienteNoEncontradoError(dni)
        if not medico:
            raise MedicoNoDisponibleError(matricula)
        # Validar especialidad
        especialidad_obj = None
        for esp in medico.obtener_especialidades():
            if esp.obtener_especialidad == especialidad:
                especialidad_obj = esp
                break
        if not especialidad_obj:
            raise ValueError("El médico no tiene la especialidad solicitada")
        # Validar día
        dia = self.obtener_dia_semana_en_espanol(fecha_hora) # obtener el día de la semana en español
        if not especialidad_obj.verificar_dia(dia):
            raise ValueError("El médico no atiende esa especialidad ese día")
        # Validar turno duplicado
        self.validar_turno_no_duplicado(fecha_hora)
        # Crear el turno con el string de especialidad
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos__.append(turno)
        self.__historias_clinicas__[dni].agregar_turno(turno)
        return turno

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos__
    
    # RECETAS E HISTORIAS CLÍNICAS
    def emitir_receta(self, dni:str, matricula:str, medicamentos:list[str]):
        paciente = self.__pacientes__.get(dni)
        medico = self.__medicos__.get(matricula)
        if not paciente:
            raise PacienteNoEncontradoError(dni)
        if not medico:
            raise MedicoNoDisponibleError(matricula)
        if not medicamentos or len(medicamentos) == 0:
            raise RecetaInvalidaError("La receta debe contener al menos un medicamento o indicar recomendaciones.")
        receta = Receta(paciente, medico, medicamentos, datetime.date.today())
        historia = self.__historias_clinicas__.get(dni)
        if historia:
            historia.agregar_receta(receta)
        else:
            raise ValueError("No se encontró una historia clínica para el paciente de DNI: " + dni)
        
    def obtener_historia_clinica(self, dni:str) -> HistoriaClinica:
        return self.__historias_clinicas__.get(dni)
    
    # VALIDACIONES Y UTILIDADES
    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoError(dni)
    
    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleError(matricula)
    
    def validar_turno_no_duplicado(self, fecha_hora: datetime.datetime):
        for turno in self.__turnos__:
            if turno.obtener_fecha_hora == fecha_hora:
                raise TurnoOcupadoError(fecha_hora.strftime("%Y-%m-%d %H:%M"))
            
    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime.date) -> str:
        dias_semana = {
            0: "Lunes",
            1: "Martes",
            2: "Miércoles",
            3: "Jueves",
            4: "Viernes",
            5: "Sábado",
            6: "Domingo"
        }
        return dias_semana[fecha_hora.weekday()]
    
    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> str:
        especialidades = medico.obtener_especialidades()
        if dia_semana in especialidades:
            return especialidades[dia_semana]
        else:
            raise ValueError(f"No hay especialidad disponible para {medico.obtener_nombre} el {dia_semana}.")
        
    def validar_especialidad_en_dia(medico: Medico, especialidad_solicitada: str, dia_semana: str):
        especialidad_disponible = medico.obtener_especialidades().get(dia_semana)
        if especialidad_disponible != especialidad_solicitada:
            raise ValueError(f"La especialidad {especialidad_solicitada} no está disponible para {medico.obtener_nombre} el {dia_semana}.")