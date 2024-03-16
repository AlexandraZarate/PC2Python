# Número máximo de filas que tiene el patrón
num_filas = 5

# Imprimir primera mitad del patrón
for i in range(1,num_filas+1):
    #Imprimir i asteriscos en cada fila
    for j in range(1,i+1):
        print("*",end=" ")
    print()
# Imprimir segunda mitad del patrón
for i in range(num_filas -1,0,-1):
    #Imprimir i asteriscos en cada fila
    for j in range(1,i+1):
        print("*",end=" ")
    print()    