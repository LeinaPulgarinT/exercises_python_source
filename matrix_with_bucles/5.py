matrix = []
M = int(input('Ingrese el número de filas: '))
N = int(input('Ingrese el número de columnas: '))

for i in range(M):
    matrix.append([])
    for j in range(N):
        matrix[i].append(0) 
print()
print()

matrix[1][0] = 1
matrix[0][1] = 1

print()

for row in matrix:
    print('[', end=' ')
    for element in row:
        print('{:4}'.format(element), end="   ") 
    print(']')
print()

count = 0
for i in range(M):
    for j in range(N):
        if matrix[i][j] != 0:
            count += 1
porcentage = (count * 100) / (N*M)
print(f'{porcentage}% ')

if porcentage < 20:
    print('Es rala')
else:
    print('No es rala')