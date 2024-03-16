# listado de números que cumplen con las condiciones del problema
numeros_divisibles_y_multiplos= []
# Poner el rango de números a tomar
for numero in range(1500,2701):
    # Verificar la divisibilidad y multiplicidad
    if numero % 7 == 0 and numero % 5 == 0:
       # añadir al listado los que cumplen
        numeros_divisibles_y_multiplos.append(numero)

# Finalizar con los números que cumplen con las condiciones
print("Los números divisibles que cumplen las condiciones de ser divisibles por 7, múltiples de 5 y estar en el rango de 1500 a 2700 son:")
print(numeros_divisibles_y_multiplos)
