def contar_digitos(numero,digito):
    numero_str=str(numero)
    contador = 0
    for d in numero_str:
        if d == str(digito):
            contador +=1
    return contador

# Ejemplo del uso de la función
numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese un dígito a buscar: "))

# Mostrar el resultado
cantidad = contar_digitos(numero,digito)
print(f"Número ingresado: {numero} y Dígito: {digito}")
print(f"Cantidad de veces {digito} en el número: {cantidad}")