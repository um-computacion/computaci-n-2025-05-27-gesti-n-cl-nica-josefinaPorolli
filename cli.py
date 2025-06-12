import datetime
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.especialidad import Especialidad
from clases.turno import Turno
from clases.receta import Receta
from clases.historiaClinica import HistoriaClinica
from excepciones.exceptions import *

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
            # Agregar paciente
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
            # Agregar médico
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

        elif opcion == '3':
            # Validar y agendar turno
            dni_paciente = input("Ingrese el DNI del paciente: ").strip()
            matricula_medico = input("Ingrese la matrícula del médico: ").strip()
            especialidad = input("Ingrese la especialidad para el turno: ").strip()
            fecha_hora_str = input("Ingrese la fecha y hora (dd/mm/aaaa hh:mm): ").strip()

            # Convertir string a datetime
            try:
                fecha_hora = datetime.datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M")
            except ValueError:
                print("Error: Fecha y hora inválidas. Ingrese un formato válido (dd/mm/aaaa hh:mm).")
                continue

            # Buscar paciente y médico
            lista_pacientes = clinica.obtener_pacientes() # devuelve la lista de pacientes
            lista_medicos = clinica.obtener_medicos() # devuelve la lista de médicos

            for pacientei in lista_pacientes:
                if pacientei.obtener_dni == dni_paciente:
                    paciente = pacientei
                    break
                else:
                    raise PacienteNoEncontradoError(dni_paciente)
            
            for medicoi in lista_medicos:
                if medicoi.obtener_matricula == matricula_medico:
                    medico = medicoi
                    break
                else:
                    raise MedicoNoDisponibleError(matricula_medico)

            try:
                # Buscar paciente, médico, agendar turno...
                clinica.agendar_turno(dni_paciente, matricula_medico, especialidad, fecha_hora)
                print("Turno agendado correctamente.\n")
            except PacienteNoEncontradoError as e:
                print(f"Error: {e}")
            except MedicoNoDisponibleError as e:
                print(f"Error: {e}")
            except ValueError as ve:
                print(f"Error: {ve}")
            except TypeError as te:
                print(f"Error de tipo de dato: {te}")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == '4':
            # Agregar especialidad a un médico
            matricula = input("Ingrese la matrícula del médico: ").strip()
            tipo_especialidad = input("Ingrese tipo de especialidad: ").strip()
            dias_str = input("Ingrese días disponibles (separados por comas): ").strip()
            DIAS_VALIDOS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] # se hace la misma validación de días que al agregar especialidad al médico en agregar médico

            dias = []
            for dia_ingresado in dias_str.split(','):
                dia = dia_ingresado.strip().capitalize()
                if dia == "Miercoles":
                    dia = "Miércoles"
                elif dia == "Sabado":
                    dia = "Sábado"
                dias.append(dia)

            # Validación
            for dia in dias:
                if dia not in DIAS_VALIDOS:
                    raise ValueError(f"Día {dia} inválido. Los días válidos son: {', '.join(DIAS_VALIDOS)}")

            # crear especialidad
            especialidad = Especialidad(tipo_especialidad, dias)
            try:
                clinica.agregar_especialidad_a_medico(matricula, especialidad)
                print("Especialidad agregada correctamente al médico.\n")
            except MedicoNoDisponibleError as e:
                print(f"Error: {e}")
            except ValueError as ve:
                print(f"Error: {ve}")
            except TypeError as te:
                print(f"Error de tipo de dato: {te}")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == '5':
            # Solicita DNI de paciente, matrícula de médico y medicamentos, luego registra la receta.
            dni_paciente = input("Ingrese el DNI del paciente: ").strip()
            matricula_medico = input("Ingrese la matrícula del médico: ").strip()
            medicamentos_str = input("Ingrese los medicamentos (separados por comas): ").strip()

            # Procesar lista de medicamentos
            medicamentos = [med.strip() for med in medicamentos_str.split(',') if med.strip()]

            try:
                clinica.emitir_receta(dni_paciente, matricula_medico, medicamentos) # también se agrega a la historia clínica del paciente
                print("Receta emitida correctamente.\n")
            except PacienteNoEncontradoError as e:
                print(f"Error: {e}")
            except MedicoNoDisponibleError as e:
                print(f"Error: {e}")
            except RecetaInvalidaError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()