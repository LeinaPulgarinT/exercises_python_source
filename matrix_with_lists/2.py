
col_row = int(input('ingrese el numero de filas y columnas: '))

# Crear una matriz cero:
matrix = [[0 for i in range(col_row)] 
for j in range(col_row)]


# Llenar matriz:
matrix_full = [[int(input('Valor: ')) for i in range(col_row)] 
for j in range(col_row)]
print(matrix_full)

# Diagonal principal
main_diagonal = [matrix_full[i][i] for i in range(col_row)]
print(main_diagonal)

# Algoritmo para sacar la diagonal secundaria:
second_diagonal = [matrix_full[i][-(i+1)]for i in range(col_row)]
print(second_diagonal)


# Algoritmo para sacar la triangular superior:










