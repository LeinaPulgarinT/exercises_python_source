matrix = []
M = int(input('Ingrese el número de filas: '))
N = int(input('Ingrese el número de columnas: '))

for i in range(M):
    matrix.append([])
    for j in range(N):
        matrix[i].append(int(input('Ingrese un elemento: '))) 
print()
print()

for fila in matrix:
    print('[', end=' ')
    for elemento in fila:
        print('{:4}'.format(elemento), end="   ") 
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
suma = 0
count = 0
lista = []
for i in range(M):
    for j in range(N):
        suma = suma + matrix[i][j]
    promedio = suma / (len(matrix[i]))
    lista.append(promedio)
    suma = 0
print(f"los promedios por fila son los siguientes: \n{lista}")

#Determinar el promedio por columna:
add_col = 0
count_col = 0
list_count = []
for i in range(N):
    for j in range(M):
        add_col = add_col + matrix[j][i]
    mean_col = add_col / (len(matrix[j]))
    list_count.append(mean_col)
    add_col = 0
print(f"los promedios por columna son los siguientes: \n{list_count}")
