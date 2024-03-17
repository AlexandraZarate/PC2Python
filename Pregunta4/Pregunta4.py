# Función para ingresar las calificaciones de los alumnos
def ingresar_calificaciones():
    calificaciones=[]
    for i in range(3):
        calificacion=float(input(f"Ingrese la calificación {i+1} del alumno: "))
        calificaciones.append(calificacion)
    return calificaciones

# Función principal del programa
def main():
    # Pedir introducir al usuario la cantidad de alumnos
    n = int(input("Ingrese la cantidad de alumnos: "))

    # Listar con un diccionario para el almacen de datos de los alumnos
    alumnos = {}

    # Ingresar los datos para cada alumno
    for i in range(1, n+1):
        print(f"Ingrese los datos para el alumno {i}:")
        nombre=input("Nombre del alumno: ")
        calificaciones= ingresar_calificaciones()
        alumnos[nombre]=calificaciones

    # Presentar el listado de alumnos con sus respectivas calificaciones
    print("\nListado de alumnos y sus calificaciones: ")
    for nombre,calificaciones in alumnos.items():
        print(f"\nAlumno: {nombre}")
        print("Calificaciones: ",calificaciones)

# Llamar a la función principal del programa
if __name__ == "__main__":
    main()

