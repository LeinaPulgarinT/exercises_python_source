# matrix_one = [[6,2,7,5],[9,7,7,1],[3,1,6,2]]
# matrix_two = [[2,4,5],[5,4,2],[7,1,1],[5,3,8]]
# lo que me tiene  que devolver: [[96, 54, 81], [107, 74, 74], [63, 28, 39]]
matrix_one = []
matrix_one_row = int(input('Ingrese el número de filas de la primera matriz: '))
matrix_one_col = int(input('Ingrese el número de columnas de la segunda matriz: '))

matrix_two = []
matrix_two_row = int(input('Ingrese el número de filas de la segunda matriz: '))
matrix_two_col = int(input('Ingrese el número de columnas de la segunda matriz: '))

# Crear la primer matriz en cero:
count_matriz_one = 0
for i in range(matrix_one_row):
    matrix_one.append([])
    for j in range(matrix_one_col):
        matrix_one[i].append(count_matriz_one)
        count_matriz_one += 1
print()
print()


# Crear la seguna matriz en cero:
count_matriz_two = 0
for i in range(matrix_two_row):
    matrix_two.append([])
    for j in range(matrix_two_col):
        matrix_two[i].append(count_matriz_two)
        count_matriz_two += 2 
print()
print()

# Organizo la primera matriz:  
for row in matrix_one:
    print('[', end=' ')
    for element in row:
        print('{:4}'.format(element), end="   ") 
    print(']')
    print()
    print()
    print()
print()

# Organizo la segunda matriz:  
for row in matrix_two:
    print('[', end=' ')
    for element in row:
        print('{:4}'.format(element), end="   ") 
    print(']')
    print()
    print()
    print()
print()

# Suma de las dos matrices:
if len(matrix_one) == len(matrix_two) and len(matrix_one[0]) == len(matrix_two[0]):
    matrix_resulting_sum = []
    sum = 0
    for i in range(len(matrix_one)):
        matrix_resulting_sum.append([])
        for j in range(len(matrix_one[0])):
            sum = matrix_one[i][j] + matrix_two[i][j]
            matrix_resulting_sum[i].append(sum)
    print(matrix_resulting_sum)
else:
    print('No se pueden sumar las matrices')
print()
print()


# Multiplicacion de las dos matrices:
if len(matrix_one) == len(matrix_two[0]):
    matrix_three = []
    #sumatoria = 0
    for i in range(len(matrix_one)):
        matrix_three.append([])
        for j in range(len(matrix_two[0])):
            matrix_three[i].append(0)
            for k in range(len(matrix_one[0])):
                matrix_three[i][j] += matrix_one[i][k] * matrix_two[k][j]
    print(matrix_three)
else:
    print('La matriz no se puede multiplicar')
    