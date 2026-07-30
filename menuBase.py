print("Bienvenido a DriveSafe")
def menu():
    print("""---Sistema de evaluaciones Drivesafe
    1. Registre evaluaciones practicas de conducciones.
    2. Consultar evaluaciones por estudiante.
    3. calcular promedio general.
    4. salir
    """)

def menuBase():
    while True:
        menu()
        opcion = int(input("\nSeleccione la opcion que desea ejecutar: "))

        if opcion == 1:
            import registroEvaluacionesP
            registroEvaluacionesP.menuRegistroEstudiantes()
        elif opcion == 2:
            import registroEvaluacionesP
            import registroEvaluacionesP
            nombre = input("Ingrese el nombre del estudiante: ").title().strip()
            datos = registroEvaluacionesP.buscarEstudiante(nombre)
            if datos:
                print(f"\nEvaluaciones de {nombre}:")
                print(f"- {datos['fecha']} | Instructor: {datos['instructor']} | Calificación: {datos['calificacion']}")
            else:
                print(f"\nNo se encontró ningún estudiante llamado {nombre}.")
        elif opcion == 3:
            import registroEvaluacionesP
            print(f"Promedio: {registroEvaluacionesP.promedioCalificaciones():.2f}")
        elif opcion == 4:
            print("\nGracias por usar DriveSafe, vuelva pronto.")
            break

if __name__ == "__main__":
    menuBase()