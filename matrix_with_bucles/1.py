"""
1). Leer una matriz A de orden M x N y un número K. Multiplicar todos los elementos de la matriz por el número K. Mostrar la matriz resultante
"""

M = int(input("Ingrese el número de filas: "))
N = int(input("Ingrese el número de columnas: "))
K = int(input("Ingrese un número, para multiplicarlo por cada uno de los elementos de la matriz: "))

matriz = []


for i in range(M):
    matriz.append([])
    for j in range(N):
       valor = int(input(f'ingrese en la fila {i}, la columna {j}: ')) 
       matriz[i].append(valor * K)

print()
for fila in matriz:
    print('[', end=' ')
    for elemento in fila:
        print('{:4}'.format(elemento), end="   ") 
    print(']')
print()
