# falta terminarlo: 
n = int(input('Ingrese el numero de estudiantes: '))
if n >= 2 and n <= 5:
    main_list = []
    for i in range(n):
        main_list.append([])
        name = input('Ingrese el nombre: ')
        score = float(input('Ingrese el puntaje: '))
        for j in range(1):
            main_list[i].append(name)
            main_list[i].append(score)
    
    
    
    for i in range(len(main_list)):
        small = main_list[0][1]
        for j in range(1):
            if main_list[i][1] < small:
                small = main_list[i][1]
    print(small)

    def take_second(elem):
        return elem[1]
    sec_small = 0
    lista = sorted(main_list, key = take_second)
    print(lista)
    min = lista[1][1]
    for i in range(len(lista)):
        for j in range(1):
            if lista[i][j] != min:
                min = lista[i+1][j]
    print(min) # Estaba Acá

    """
    """