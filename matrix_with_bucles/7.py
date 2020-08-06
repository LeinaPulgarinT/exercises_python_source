matrix = []
M = int(input('Ingrese el número de filas de matriz: '))
N = int(input('Ingrese el número de columnas de la matriz: '))
count = 1
for i in range(M):
    matrix.append([])
    for j in range(N):
        matrix[i].append(count)
        count += 1
print()
print()

# Organizo la  matriz:  
for row in matrix:
    print('[', end=' ')
    for element in row:
        print('{:4}'.format(element), end="   ") 
    print(']')
    print()
    print()
    print()
print()

# Eliminar una fila: 
X = int(input('Ingrese el número de la fila que desea eliminar, tenga en cuanta que las filas empiezan desde Cero.'))
sumatoria = []
for i in range(len(matrix)):
    if matrix[X] == matrix[i]:
        continue
    else:
        sumatoria.append(matrix[i])
matrix = sumatoria
#print(matrix)

# Eliminar una columna: 
Y = int(input('Ingrese el número de la columna que desea eliminar, tenga en cuanta que las filas empiezan desde Cero. '))
#Y += 1
sumatoria = []
for i in range(len(matrix)):
    sumatoria.append([])
    for j in range(len(matrix[0])):
        if matrix[i][Y] == matrix[i][j]:
            continue
        else:
            sumatoria[i].append(matrix[i][j])
matrix = sumatoria
for row in matrix:
    print('[', end=' ')
    for element in row:
        print('{:4}'.format(element), end="   ") 
    print(']')
    print()
    print()
    print()
print()

# Insertar una nueva fila:
new_row = []
for i in range(N):
    element = int(input('Ingrese un numero: '))
    new_row.append(element)
print(new_row)

A = int(input(f'Ingrese la posición de la fila que quiere cambiar, tenga encuenta que: posiciones >= 0 y < {M}: '))
print()
for i in range(len(matrix)):
    if matrix[i] == matrix[A]:
        continue
    else:
        matrix[A] = new_row

for row in matrix:
    print('[', end=' ')
    for element in row:
        print('{:4}'.format(element), end="   ") 
    print(']')
    print()