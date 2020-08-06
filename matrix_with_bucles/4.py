matrix = []
M = int(input('Ingrese el número de filas: '))
N = int(input('Ingrese el número de columnas: '))

for i in range(M):
    matrix.append([])
    for j in range(N):
        matrix[i].append(int(input('Ingrese un elemento: '))) 
print()
print()

for row in matrix:
    print('[', end=' ')
    for element in row:
        print('{:4}'.format(element), end="   ") 
    print(']')
print()


# Determinar si la matriz es cuadrada:
if N > 1 and M > 1 and  N == M:
    print('La matriz es cuadrada')
    print()
elif N > 0 and M > 0:
    print('La matriz no es cuadrada')
else: 
    print('No es matriz')

# Determinar el promedio por fila:
sum = 0
count = 0
mean_row = []
for i in range(M):
    for j in range(N):
        sum = sum + matrix[i][j]
    mean = sum / (len(matrix[i]))
    mean_row.append(mean)
    sum = 0
print(f"los promedios por fila son los siguientes: \n{mean_row}")

#Determinar el promedio por columna:
add_col = 0
count_col = 0
mean_col = []
for i in range(N):
    for j in range(M):
        add_col = add_col + matrix[j][i]
    mean = add_col / (len(matrix[j]))
    mean_col.append(mean)
    add_col = 0
print(f"los promedios por columna son los siguientes: \n{mean_col}")
