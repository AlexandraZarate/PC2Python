# Función para verificar si un número es primo o no
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2,int(numero**0.5)+ 1):
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso de la función
numero = int(input("ingrese un número: "))
if es_primo(numero):
    print(numero,"es un número primo.")
else:
    print(numero,"no es un número primo.") 