# Función de acortamiento de palabras omitiendo vocales
def omitir_vocales(cadena):
    vocales = "AEIOUaeiou"
    resultado = ""
    for caracter in cadena:
        if caracter not in vocales:
            resultado += caracter
    return resultado

#  Pedir al usuario que ingrese una cadena de texto 
texto = input("Ingrese una cadena de texto: ")
# Obtener y presentar el texto
texto_sin_vocales = omitir_vocales(texto)
print("Texto con vocales omitidas: ",texto_sin_vocales)         