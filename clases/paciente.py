import datetime # se importa datetime para manejar fechas
class Paciente:
    # CONSTRUCTOR
    def __init__(self, nombre:str, dni:str, fecha_nacimiento:datetime.date):
        self.__nombre__ = nombre
        self.__dni__ = dni
        self.__fecha_nacimiento__ = fecha_nacimiento
    
    # GETTERS
    @property # para volverlo un atributo de solo lectura
    def obtener_dni(self) -> str:
        return self.__dni__
    
    # REPRESENTACION
    def __str__(self) -> str:
        return f"Paciente: {self.__nombre__}\nDNI: {self.__dni__}\nFecha de Nacimiento: {self.__fecha_nacimiento__}"
