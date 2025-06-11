import datetime
from clases.clinica import Clinica
from clases.paciente import Paciente

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
                    print("Fecha inválida. Ingrese un formato válido.")
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


if __name__ == "__main__":
    main()