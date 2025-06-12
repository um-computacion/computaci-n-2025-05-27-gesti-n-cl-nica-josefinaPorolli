import datetime # se importa datetime para manejar fechas
class Paciente:
    # CONSTRUCTOR
    def __init__(self, nombre:str, dni:str, fecha_nacimiento:datetime.date):
        # VALIDACIONES
        # Validar existencia de datos obligatorios
        if not nombre or not dni or not fecha_nacimiento:
            raise ValueError("Faltan datos obligatorios del paciente")
        # Validar tipo de datos
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena")
        if not isinstance(dni, str):
            raise TypeError("El DNI debe ser una cadena")
        if not isinstance(fecha_nacimiento, datetime.date):
            raise TypeError("La fecha de nacimiento debe ser un objeto datetime.date")
        
        self.__nombre__ = nombre
        self.__dni__ = dni
        self.__fecha_nacimiento__ = fecha_nacimiento
    
    # GETTERS
    @property # para volverlo un atributo de solo lectura
    def obtener_dni(self) -> str:
        return self.__dni__
    
    @property
    def obtener_nombre(self) -> str: # se consideró la posibilidad de agregar esto para mayor legibilidad
        return self.__nombre__
    
    # REPRESENTACION
    def __str__(self) -> str:
        return f"---------\nPaciente: {self.__nombre__}\nDNI: {self.__dni__}\nFecha de Nacimiento: {self.__fecha_nacimiento__}\n---------"
