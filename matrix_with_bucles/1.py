"""
1). Leer una matriz A de orden M x N y un número K. Multiplicar todos los elementos de la matriz por el número K. Mostrar la matriz resultante
"""

M = int(input("Ingrese el número de filas: "))
N = int(input("Ingrese el número de columnas: "))
K = int(input("Ingrese un número, para multiplicarlo por cada uno de los elementos de la matriz: "))

matrix = []


for i in range(M):
    matrix.append([])
    for j in range(N):
       value = int(input(f'ingrese en la fila {i}, la columna {j}: ')) 
       matrix[i].append(value * K)

print()
for row in matrix:
    print('[', end=' ')
    for element in row:
        print('{:4}'.format(element), end="   ") 
    print(']')
print()
