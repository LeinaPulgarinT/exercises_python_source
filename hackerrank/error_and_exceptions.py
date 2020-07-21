number_test = int(input('Ingrese el numero de casos de prueba: '))

if number_test > 0 and number_test < 10:
    count = 1 
    
    while count <= number_test:
        x = int(input('Ingrese el numerador: '))
        y = input('Ingrese el denominador: ')
        if int(y) != 0 and int(y) != int() and y == str():
            print('Error Code: invalid literal for int() with base 10: ' )
        elif int(y) == int() and int(y) == 0:
            print("Error Code: integer division or modulo by zero")
        else: 
           
            d = x // int(y)
            print(d)
        count = count + 1

