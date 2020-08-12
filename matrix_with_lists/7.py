# Matriz para hacer las pruebas
matrix = [[6,2,7,5],[9,7,8,1],[3,1,6,2]]

# Eliminar una fila:
def delete_row(matrix):
    X = int(input('Ingrese el número de la fila que desea eliminar, \
    tenga en cuanta que las filas empiezan desde Cero.'))
    matrix_aux = [matrix[i] for i in range(len(matrix)) \
    if matrix[X] != matrix[i]]
    matrix = matrix_aux
    return matrix
#print(delete_row(matrix))

# Insertar una nueva fila:
def insert_row(matrix):
    new_row = [int(input('Ingrese un numero: ')) for i in range(len(matrix[0]))]
    A = int(input(f'Ingrese la posición de la fila que quiere cambiar, \
    tenga encuenta que: posiciones >= 0 y < {len(matrix)}: '))
    matrix_aux = [new_row if matrix[i] == matrix[A] else matrix[i] 
    for i in range(len(matrix))]
    matrix = matrix_aux
    return matrix
#print(insert_row(matrix))

# Eliminar columna:
def delete_col(matrix):
    Y = int(input('Ingrese el número de la columna que desea eliminar, \
    tenga en cuanta que las columnas empiezan desde Cero. '))
    matrix_aux = [[matrix[i][j] for j in range(len(matrix[0]))
    if matrix[i][Y] != matrix[i][j]] for i in range(len(matrix))]
    matrix = matrix_aux
    return matrix
#print(delete_col(matrix))

# Insertar columna:
def insert_col(matrix):
    new_col = [int(input('Ingrese un numero: ')) for i in range(len(matrix))]
    B = int(input(f'Ingrese la posición de la columna que quiere cambiar, \
    tenga encuenta que: posiciones >= 0 y < {len(matrix[0])}: '))
    matrix_aux = [[new_col[i] if matrix[i][B] == matrix[i][j] else matrix[i][j] \
    for j in range(len(matrix[0]))] for i in range(len(matrix))]
    matrix = matrix_aux
    return matrix_aux
#print(insert_col(matrix))