import json
import os

ARCHIVO = 'estudiantes.json'

# Cargar estudiantes desde el archivo JSON
def cargar_estudiantes():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r') as file:
            return json.load(file)
    return []

# Guardar estudiantes en el archivo JSON
def guardar_estudiantes(estudiantes):
    with open(ARCHIVO, 'w') as file:
        json.dump(estudiantes, file, indent=4)

# Agregar un nuevo estudiante
def agregar_estudiante():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    carrera = input("Carrera: ")
    estudiante = {"nombre": nombre, "edad": edad, "carrera": carrera}
    estudiantes = cargar_estudiantes()
    estudiantes.append(estudiante)
    guardar_estudiantes(estudiantes)
    print("Estudiante guardado correctamente.")

# Mostrar todos los estudiantes
def mostrar_estudiantes():
    estudiantes = cargar_estudiantes()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for idx, est in enumerate(estudiantes, 1):
        print(f"{idx}. {est['nombre']} - {est['edad']} años - {est['carrera']}")

# Menú principal
def menu():
    while True:
        print("\n1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
