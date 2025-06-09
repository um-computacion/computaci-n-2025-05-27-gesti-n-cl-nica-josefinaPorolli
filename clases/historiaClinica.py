from paciente import Paciente
from turno import Turno
from receta import Receta

class HistoriaClinica:
    # CONSTRUCTOR
    def __init__(self, paciente:Paciente, turnos:list[Turno], recetas:list[Receta]):
        self.paciente = paciente
        self.turnos = turnos
        self.recetas = recetas
    
    # SETTERS
    def agregar_turno(self, turno:Turno):
        self.turnos.append(turno)
    
    def agregar_receta(self, receta:Receta):
        self.recetas.append(receta)
    
    # GETTERS
    @property
    def obtener_turnos(self) -> list[Turno]:
        return self.turnos
    
    @property
    def obtener_recetas(self) -> list[Receta]:
        return self.recetas
    
    # REPRESENTACION
    def __str__(self) -> str:
        turnos_str = "\n".join(str(turno) for turno in self.turnos)
        recetas_str = "\n".join(str(receta) for receta in self.recetas)
        return f"Historia Clinica de {self.paciente.nombre}\nTURNOS:\n{turnos_str}\nRECETAS:\n{recetas_str}"