"""
Por si quiere generar la matriz:
M = int(input('Ingrese el número de filas: '))
N = int(input('Ingrese el número de columnas: '))

# Generar matriz:
matrix = [[j+1 for j in range(N)] 
                for i in range(M)] 
print('Matriz generada: ')
print(matrix)
"""

# Matriz para hacer pruebas
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
print()
print('Promedio Matriz por fila: ')
print(mean_row)
print()

# Determinar el promedio por columna
mean_col = [promedio(*[row[i] for row in matrix]) for i in range(len(matrix[0]))]
print('Promedio Matriz por columna: ')
print(mean_col)


