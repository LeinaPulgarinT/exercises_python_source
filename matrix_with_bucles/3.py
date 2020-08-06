x = []
A = int(input('Ingrese el número de filas: '))
B = int(input('Ingrese el número de columnas: '))
print()
print()
for i in range(A):
    x.append([])
    for j in range(B):
        x[i].append(0)

count = 1
for i in range(A):
    for j in range(B):
        x[i][j]= count
        count += 1
#print(x)



# Organizo la matriz:  
for fila in x:
    print('[', end=' ')
    for elemento in fila:
        print('{:4}'.format(elemento), end="   ") 
    print(']')
    print()
    print()
    print()
print()

# Algoritmo para hacer la traspuesta de la matriz: 
transposed_matrix = []
count = 0
for i in range(len(x[0])):
    transposed_matrix.append([])
    for j in range(len(x)):
        transposed_matrix[i].append(x[j][i])
print(lista)