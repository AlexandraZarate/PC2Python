# Función para cacular el factorial de un número entero no negativo
def factorial(numero):
    if numero < 0:
        return "El factorial no admite cálculos para números negativos."
    resultado = 1
    for i in range(1,numero + 1):
        resultado *=i
    return resultado

# Ejemplo del uso de la función
numero = int(input("Ingrese un número entero no negativo: "))
print("El factorial de",numero,"es:",factorial(numero))