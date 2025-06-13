# Excepción de paciente no encontrado
class PacienteNoEncontradoError(Exception):
    def __init__(self, dni: str):
        super().__init__(f"Paciente con DNI {dni} no encontrado.")
        self.dni = dni

# Excepción de médico no disponible
class MedicoNoDisponibleError(Exception):
    def __init__(self, matricula: str):
        super().__init__(f"Médico con matrícula {matricula} no disponible.")
        self.matricula = matricula

# Excepción de turno ocupado
class TurnoOcupadoError(Exception):
    def __init__(self, fecha_hora: str):
        super().__init__(f"Turno ya ocupado para la fecha y hora {fecha_hora}.")
        self.fecha_hora = fecha_hora

# Excepción de receta inválida
class RecetaInvalidaError(Exception):
    def __init__(self, mensaje: str):
        super().__init__(f"Receta inválida: {mensaje}")
        self.mensaje = mensaje