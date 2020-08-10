#M = int(input('Ingrese el número de filas: '))
#N = int(input('Ingrese el número de columnas: '))

# Llenar la matriz con numeros:
"""
matrix = [[j+1 for j in range(N)] 
                for i in range(M)] 
print(matrix)
"""
#matrix = [[1, 2, 3], [15, 8, 9, 60, 6], [1, 2]]
matrix = [[1, 2, 4], [15, 8, 5], [1, 2, 5], [30, 5, 7]]

# Determinar el promedio por fila:
def promedio(*args):
    sum = 0
    count = 0
    for i in args:
        count += 1
        sum += i 
    return sum/count
mean_row = [promedio(*matrix[i]) for i in range(len(matrix))]
#print(mean_row)

# Determinar el promedio por columna
mean_col = [promedio(*[row[i] for row in matrix]) for i in range(len(matrix[0]))]
print(mean_col)

# Para entender mejor como funciona: 
#mean_col = [ for col in range(len(matrix[0])) for row in matrix]
#mean_col = [[row[col] for row in matrix] for col in range(len(matrix[0]))]


