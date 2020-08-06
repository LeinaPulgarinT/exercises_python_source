M = int(input('Ingrese el número de filas: '))
N = int(input('Ingrese el número de columnas: '))

# Llenar la matriz con numeros:
matrix = [[j+1 for j in range(N)] 
                for i in range(M)] 
print(matrix)

# Determinar el promedio por fila:
