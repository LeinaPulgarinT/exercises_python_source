
M = int(input("Ingrese el número de filas de la primera matriz: "))
N = int(input("Ingrese el número de columnas de la primera matriz: "))

matrix_one = [[int(input('Valor: ')) for j in range(N)] 
for i in range(M)]
#print(matrix_one)

A = int(input("Ingrese el número de filas de la segunda matriz: "))
B = int(input("Ingrese el número de columnas de la segunda matriz: "))
matrix_two = [[int(input('Valor: ')) for j in range(B)] 
for i in range(A)]

#matrix_one = [[6,2,7,5],[9,7,7,1],[3,1,6,2]]
#matrix_two = [[2,4,5,4],[5,4,2,5],[7,1,1,2]]
#matrix_two = [[2,4,5],[5,4,2],[7,1,1],[2,4,5]]

#matrix_one = [[1,2,3], [4,5,6]]
#matrix_two = [[1,2], [3,4], [5,6]]

# Algoritmo para sumar dos matrices:
if len(matrix_one) == len(matrix_two) and \
len(matrix_one[0]) == len(matrix_two[0]):
    sum = [[matrix_one[i][j] + matrix_two[i][j] 
        for j in range(len(matrix_one[0]))] 
        for i in range(len(matrix_one))]
    print(sum)
else:
    print('No se pueden sumar las matrices')


# Algoritmo para multiplicar dos matrices:
def mean(*args):
    sum = 0
    for i in args:
        sum += i 
    return sum

if len(matrix_one) == len(matrix_two[0]):
    mult = [[mean(*[matrix_one[i][k] * matrix_two[k][j] 
            for k in range(len(matrix_one[0]))]) 
            for j in range(len(matrix_two[0]))] 
            for i in range(len(matrix_one))]
    print(mult)
else:
     print('La matriz no se puede multiplicar')


