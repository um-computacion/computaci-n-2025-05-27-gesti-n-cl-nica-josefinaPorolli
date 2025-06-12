import datetime
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.especialidad import Especialidad

def menu():
    print('''
    --- Menú Clínica ---
    1) Agregar paciente
    2) Agregar médico
    3) Agendar turno
    4) Agregar especialidad
    5) Emitir receta
    6) Ver historia clínica
    7) Ver todos los turnos
    8) Ver todos los pacientes
    9) Ver todos los médicos
    0) Salir
    ''')

def main():
    clinica = Clinica({}, {}, [], {})
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            print("Saliendo del programa...")
            break
        
        elif opcion == '1':
            try:
                nombre = input("Ingrese nombre del paciente: ").strip() # strip elimina espacios al inicio y al final
                dni = input("Ingrese DNI del paciente: ").strip()
                fecha_str = input("Ingrese fecha de nacimiento (dd/mm/aaaa): ").strip()

                # Convertir string a datetime.date
                try:
                    fecha_nac = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date() # strptime convierte un string a un objeto datetime
                except ValueError:
                    print("Error al cargar. Fecha inválida. Ingrese un formato válido.")
                    continue

                # Crear paciente y agregar
                paciente = Paciente(nombre, dni, fecha_nac)
                clinica.agregar_paciente(paciente)
                print("Paciente agregado correctamente.\n")

            # Excepciones para errores comunes
            except ValueError as ve:
                print(f"Error: {ve}")
            except TypeError as te:
                print(f"Error de tipo de dato: {te}")
            except Exception as e:
                print(f"Error inesperado: {e}")
        
        elif opcion == '2':
            try:
                nombre = input("Ingrese nombre del médico: ").strip()
                matricula = input("Ingrese matrícula del médico: ").strip()
                especialidades = [] # se inicializa la lista de especialidades
                print("REGISTRO DE ESPECIALIDADES")
                DIAS_VALIDOS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] # me cansé de buscar forma para que se validen los días sin las tildes :(

                while True:
                    tipo_especialidad = input("Ingrese tipo de especialidad (o '0' para terminar): ").strip()
                    if tipo_especialidad == '0':
                        break

                    dias_str = input("Ingrese días disponibles (separados por comas): ").strip()

                    dias = []
                    for dia_ingresado in dias_str.split(','): # primero se separa por comas
                        dia = dia_ingresado.strip().capitalize() # antes el capitalize quería poner en mayúscula el espacio xd
                        if dia == "Miercoles": # para agregar la tilde
                            dia = "Miércoles"
                        elif dia == "Sabado":
                            dia = "Sábado"
                        dias.append(dia)
                    print(dias)

                    # Validación
                    for dia in dias:
                        if dia not in DIAS_VALIDOS:
                            raise ValueError(f"Día {dia} inválido. Los días válidos son: {', '.join(DIAS_VALIDOS)}")

                    especialidad = Especialidad(tipo_especialidad, dias)
                    especialidades.append(especialidad)

                # Crear médico y agregar
                medico = Medico(nombre, matricula, especialidades)
                clinica.agregar_medico(medico)
                print("Médico agregado correctamente.\n")

            except ValueError as ve:
                print(f"Error: {ve}")
            except TypeError as te:
                print(f"Error de tipo de dato: {te}")
            except Exception as e:
                print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()