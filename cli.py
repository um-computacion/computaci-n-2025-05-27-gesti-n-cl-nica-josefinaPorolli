from clases.clinica import Clinica


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

if __name__ == "__main__":
    main()