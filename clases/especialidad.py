class Especialidad:
    # Para tomar días válidos
    # CONSTRUCTOR
    def __init__(self, tipo:str, dias:list):
        if not tipo or not dias:
            raise ValueError("Faltan datos de especialidad")
        if not isinstance(tipo, str) or not isinstance(dias, list):
            raise TypeError("Nombre debe ser str y días debe ser una lista")
        self.__tipo__ = tipo
        self.__dias__ = dias
    
    # GETTERS
    @property
    def obtener_especialidad(self) -> str: #devuelve el nombre de la especialidad
        return self.__tipo__
    
    @property
    def obtener_dias(self) -> list: # se agregó este getter para obtener los días desde la clase Médico
        return self.__dias__
    
    # VALIDACIONES
    def verificar_dia(self, dia:str) -> bool: # devuelve true si la especialidad está disponible en el día proporcionado. En caso contrario, devuelve false
        return dia in self.__dias__ # si día está en la lista de días
    
    # REPRESENTACION
    def __str__(self) -> str:
        dias_str = '\n'.join(self.__dias__)  # convierte la lista de días en un string legible
        return f"Especialidad: {self.__tipo__}\nDías disponibles:\n{dias_str}"