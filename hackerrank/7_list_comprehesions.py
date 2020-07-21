"""
link del enunciado del punto:
https://www.hackerrank.com/challenges/list-comprehensions/problem
"""

x = int(input('Ingrese Cero ó 1 por favor: '))
y = int(input('Ingrese Cero ó 1 por favor: '))
z = int(input('Ingrese Cero ó 1 por favor: '))
n = int(input('Ingrese el valor de n: '))

for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
            if i + j + k != 0:
                new_list.append([i, j, k])
print(new_list)