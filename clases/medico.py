from especialidad import Especialidad # Se importa la clase Especialidad para poder usarla en la clase Medico
class Medico:
    # CONSTRUCTOR
    def __init__(self, nombre:str, matricula:str, especialidades:list):
        self.__nombre__ = nombre
        self.__matricula__ = matricula
        self.__especialidades__ = especialidades # Se traerá una lista de especialidades de la clase Especialidad
    
    # SETTERS
    def agregar_especialidad(self, especialidad:Especialidad): # Cuando se cree la clase Especialidad, se podrá agregar una especialidad
        self.__especialidades__.append(especialidad)
    
    # GETTERS
    @property # para volverlo un atributo de solo lectura
    def obtener_matricula(self) -> str:
        return self.__matricula__
    
    def obtener_especialidad_para_dia(self, dia:str) -> str:
        for especialidad in self.__especialidades__:
            if dia in especialidad.__dias__:
                return especialidad.__tipo__
        return None
    
    # REPRESENTACION
    def __str__(self) -> str:
        especialidades_str = '\n'.join([especialidad.__tipo__ for especialidad in self.__especialidades__]) # Se crea un string legible para listar las especialidades
        return f"Medico: {self.__nombre__}\nMatricula: {self.__matricula__}\nEspecialidades: {especialidades_str}"