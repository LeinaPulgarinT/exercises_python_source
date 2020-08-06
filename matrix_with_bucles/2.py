matriz_cero = []
contador = 1
col_and_row = int(input('ingrese el numero de filas y columnas: '))

# Primero creo una matriz cero: 
for i in range(col_and_row):
    matriz_cero.append([])
    for j in range(col_and_row):
        matriz_cero[i].append(0)
print()

# Lleno de una secuencia de numeros:
for i in range(col_and_row):
    for j in range(col_and_row):
        matriz_cero[i][j] = contador
        contador = contador + 1

# Organizo la matriz:  
for fila in matriz_cero:
    print('[', end=' ')
    for elemento in fila:
        print('{:4}'.format(elemento), end="   ") 
    print(']')
    print()
    print()
    print()
print()

#Diagonal principal
main_diagonal = []
contador1 = 0
for i in range(col_and_row):
    main_diagonal.append(matriz_cero[i][contador1])
    contador1 = contador1 + 1
print(main_diagonal)

#Diagonal Secundaria
secondary_diagonal = []
contador2 = -1
for i in range(col_and_row):
    secondary_diagonal.append(matriz_cero[i][contador2])
    contador2 = contador2 - 1
print(secondary_diagonal)


# Algoritmo para sacar la matriz triangular superior
lista = []
count = 0
aumentar = matriz_cero[count]
for i in range(col_and_row):
    if count < i:
        lista.append(aumentar )
        count = count + 1
        aumentar = matriz_cero[count][count:]
if count == i:
    lista.append([matriz_cero[i][-1]])
print(lista)

# Algoritmo para sacar la matriz triangular inferior:
count2 = 0
lista2 = []
aumentar2 = matriz_cero[count2][count2:count2+1]
for i in range(col_and_row):
    if count2 < i :
        lista2.append(aumentar2)
        count2 = count2 + 1
        #print(count)
        aumentar2 = matriz_cero[count2][0:count2+1]
if count2 == i:
    lista2.append(matriz_cero[i])
print(lista2)