matrix_zero = []
count = 1
col_and_row = int(input('ingrese el numero de filas y columnas: '))

# Primero creo una matriz cero: 
for i in range(col_and_row):
    matrix_zero.append([])
    for j in range(col_and_row):
        matrix_zero[i].append(0)
print()

# Lleno de una secuencia de numeros:
for i in range(col_and_row):
    for j in range(col_and_row):
        matrix_zero[i][j] = count
        count = count + 1

# Organizo la matriz:  
for row in matrix_zero:
    print('[', end=' ')
    for element in row:
        print('{:4}'.format(element), end="   ") 
    print(']')
    print()
    print()
    print()
print()

#Diagonal principal
main_diagonal = []
count_one = 0
for i in range(col_and_row):
    main_diagonal.append(matrix_zero[i][count_one])
    count_one = count_one + 1
print(main_diagonal)

#Diagonal Secundaria
secondary_diagonal = []
count_two = -1
for i in range(col_and_row):
    secondary_diagonal.append(matrix_zero[i][count_two])
    count_two = count_two - 1
print(secondary_diagonal)


# Algoritmo para sacar la matriz triangular superior
upper_triang = []
count_th = 0
increase = matrix_zero[count_th]
for i in range(col_and_row):
    if count_th < i:
        upper_triang.append(increase)
        count_th = count_th + 1
        increase = matrix_zero[count_th][count_th:]
if count_th == i:
    upper_triang.append([matrix_zero[i][-1]])
print(upper_triang)

# Algoritmo para sacar la matriz triangular inferior:
count_four = 0
lower_triang = []
aumentar2 = matrix_zero[count_four][count_four:count_four+1]
for i in range(col_and_row):
    if count_four < i :
        lower_triang.append(aumentar2)
        count_four = count_four + 1
        aumentar2 = matrix_zero[count_four][0:count_four+1]
if count_four == i:
    lower_triang.append(matrix_zero[i])
print(lower_triang)