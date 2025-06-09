from paciente import Paciente
from turno import Turno
from receta import Receta

class HistoriaClinica:
    # CONSTRUCTOR
    def __init__(self, paciente:Paciente, turnos:list[Turno], recetas:list[Receta]):
        self.__paciente__ = paciente
        self.__turnos__ = turnos
        self.__recetas__ = recetas
    
    # SETTERS
    def agregar_turno(self, turno:Turno):
        self.__turnos__.append(turno)
    
    def agregar_receta(self, receta:Receta):
        self.__recetas__.append(receta)
    
    # GETTERS
    @property
    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos__
    
    @property
    def obtener_recetas(self) -> list[Receta]:
        return self.__recetas__
    
    # REPRESENTACION
    def __str__(self) -> str:
        turnos_str = "\n".join(str(turno) for turno in self.__turnos__)
        recetas_str = "\n".join(str(receta) for receta in self.__recetas__)
        return f"Historia Clinica de {self.__paciente__.__nombre__}\nTURNOS:\n{turnos_str}\nRECETAS:\n{recetas_str}"