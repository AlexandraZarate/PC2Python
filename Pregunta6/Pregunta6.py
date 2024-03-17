# Función para generar la serie de Fibonacci hasta un cierto número 
def fibonacci_hasta_limite(limite):
    fibonacci= [0,1]
    while fibonacci[-1]+ fibonacci[-2] <= limite:
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
    return fibonacci

# Presentar la seri de Fibonacci hasta 50
serie_fibonacci = fibonacci_hasta_limite(50)
print("Serie de fibonacci hasta 50: ")
print(serie_fibonacci)
