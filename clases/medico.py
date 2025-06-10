from .especialidad import Especialidad # Se importa la clase Especialidad para poder usarla en la clase Medico
class Medico:
    # CONSTRUCTOR
    def __init__(self, nombre:str, matricula:str, especialidades:list):
        # VALIDACIONES
        # Validar existencia de datos obligatorios
        if not nombre or not matricula or not especialidades:
            raise ValueError("Faltan datos obligatorios del médico")
        # Validar tipo de datos
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena")
        if not isinstance(matricula, str):
            raise TypeError("La matrícula debe ser una cadena")
        if not isinstance(especialidades, list):
            raise TypeError("Debe hacer una lista de especialidades")
        self.__nombre__ = nombre
        self.__matricula__ = matricula
        self.__especialidades__ = especialidades # Se traerá una lista de especialidades de la clase Especialidad
    
    # SETTERS
    def agregar_especialidad(self, especialidad:Especialidad):
        if not isinstance(especialidad, Especialidad):
            raise TypeError("La especialidad debe ser una instancia de la clase Especialidad")

        for esp in self.__especialidades__:
            if esp.obtener_especialidad == especialidad.obtener_especialidad:
                raise ValueError("La especialidad ya está registrada para este médico")
        
        self.__especialidades__.append(especialidad)
    
    # GETTERS
    @property # para volverlo un atributo de solo lectura
    def obtener_matricula(self) -> str:
        return self.__matricula__
    
    @property
    def obtener_nombre(self) -> str: # se consideró la posibilidad de agregar esto para mayor legibilidad
        return self.__nombre__
    
    def obtener_especialidades(self) -> list[Especialidad]:
        return self.__especialidades__
    
    def obtener_especialidad_para_dia(self, dia:str) -> str:
        for especialidad in self.__especialidades__:
            if dia in especialidad.obtener_dias:
                return especialidad.obtener_especialidad 
        return None
    
    # REPRESENTACION
    def __str__(self) -> str:
        lista = []
        for especialidad in self.__especialidades__:
            lista.append(especialidad.obtener_especialidad)
        especialidades_str = '\n'.join(lista) # Se crea un string legible para listar las especialidades
        return f"Medico: {self.__nombre__}\nMatricula: {self.__matricula__}\nEspecialidades: {especialidades_str}"