# Algoritmo para transponer una matrix:
A = int(input('Ingrese el número de filas: '))
B = int(input('Ingrese el número de columnas: '))

# Llenar la matriz con numeros:
matrix = [[j+1 for j in range(B)] 
                for i in range(A)] 
print(matrix)

# Transpuesta de una matriz:
transposed = [[j[i] for j in matrix] for i in range(A)]
print(transposed)




