numeros = []

# Uso del bucle While para permitir el ingreso de números al usuario
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO)").strip().upper()
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif respuesta == "NO":
        break
    else:
        print("Solo se admiten las respuestas: SI o NO.")

# Presentar números ingresados
print("Números ingresados:", numeros)

# Contar cantidad de números pares e impares
pares = sum (1 for num in numeros if num % 2 == 0)
impares = sum (1 for num in numeros if num % 2 !=0)

# Presentar la cantidad de números pares e impares
print("Cantidad de números pares:",pares)
print ("Cantidad de números impares:",impares)