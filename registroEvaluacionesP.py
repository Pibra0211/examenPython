import json
import os
from datetime import datetime, timedelta


def validarFecha(fechaStr):
    """Valida formato DD/MM/AAAA y que sea una fecha real."""
    if len(fechaStr) != 10:
        return False
    if fechaStr[2] != "/" or fechaStr[5] != "/":
        return False
    try:
        datetime.strptime(fechaStr, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validarCalificacion(calificacion):
    if calificacion > 100 or calificacion < 0:
        return False
    return True
archivoEstudiantes = os.path.join("data", "clientes.json")
estudiantes = {}


def cargarEstudiantes():
    
    global estudiantes
    if os.path.exists(archivoEstudiantes):
        with open(archivoEstudiantes, "r", encoding="utf-8") as archivo:
            try:
                estudiantes = json.load(archivo)
            except json.JSONDecodeError:
                estudiantes = {}
    else:
        estudiantes = {}
    return estudiantes
estudiantes = cargarEstudiantes()

def guardarEstudiantes():
    os.makedirs("data", exist_ok=True)
    with open(archivoEstudiantes, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)

def registroEstudiante():
    while True:
        nombre = input("\nDigite el nombre completo del cliente: ").title().strip()
        if nombre.replace(" ", "").isalpha():
            break
        print("\nEl nombre no puede contener numeros ni caracteres especiales.")

    while True:
        nombreInstructor = input("Ingrese el nombre completo del instructor: ").title().strip()
        if nombreInstructor.replace(" ", "").isalpha():
            break
        print("\nEl nombre no puede contener numeros ni caracteres especiales.")

    while True:
        fecha = input("\nIngrese la fecha de la clase (DD/MM/AAAA): ").strip()
        if validarFecha(fecha):
            break
        print("\nFecha inválida. Use DD/MM/AAAA con una fecha real (ej: no 31/02/2026).")

    while True:
        calificacion = int(input("\nIngrese la claficacion de la clase "))        
        if validarCalificacion(calificacion):
            break
        print("\n Calificacion invalida, debe ser mayor a 0 y menos a 100")

    datos = {
    "instructor": nombreInstructor,
    "fecha": fecha,
    "calificacion": calificacion,
    }
    estudiantes[nombre] = datos
    guardarEstudiantes()
    print(f"\nSeñor/señora {nombre}, sus datos se han registrado con exito.")
    return datos
    
def promedioCalificaciones():
    if not estudiantes:
        return 0
    suma = sum(datos["calificacion"] for datos in estudiantes.values())
    return suma / len(estudiantes)

    
def buscarEstudiante(nombre):
    return estudiantes.get(nombre)


def listarEstudiantes():
    return estudiantes


def menuRegistroEstudiantes():
    cargarEstudiantes()
    while True:
        registroEstudiante()
        while True:
            decision = input("¿Desea registrar un nuevo estudiante s/n: ").strip().lower()
            if decision in ("s", "n"):
                break
            print("\nRespuesta invalida. Debe ingresar 's' o 'n'.")
        if decision == "n":
            print(f"\nEstudiantes registrados en total: {len(estudiantes)}")
            break

    import menuBase
    menuBase.menu


if __name__ == "__main__":
    menuRegistroEstudiantes()
