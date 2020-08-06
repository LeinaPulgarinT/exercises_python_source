"""
Leer una matriz A de orden M x N y un número K. Multiplicar todos los elementos de la matriz por el número K. Mostrar la matriz resultante
"""

M = int(input("Ingrese el número de filas: "))
N = int(input("Ingrese el número de columnas: "))
K = int(input("Ingrese un número, para multiplicarlo por cada uno de los elementos de la matriz: "))

# Una forma de hacerlo
rows = [[] for i in range(M)] 
matrix = [[j*K for j in range(N)] for i in rows]
print()

# Una forma de hacerlo:
matri_two =[[i*K for i in range(N)] for num in 
[num for num in range(M)]] 
print(matriz_two)