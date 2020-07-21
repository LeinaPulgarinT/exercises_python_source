"""
link del enunciado del punto:
https://www.hackerrank.com/challenges/python-print/problem 
"""
n = int(input('Ingrese un numero: '))
# 3 formas de resolver el problema:
#1):
print(*range(1, n+1), sep='')

#2):
def give_number(number_enter):
    number = 1
    list = []
    while number <= number_enter:
        list.append(number)
        number = number + 1
    print(*list, sep='')
give_number(n)

#3):
for i in range(1, n+1):
    print(i, end='')
   

 
