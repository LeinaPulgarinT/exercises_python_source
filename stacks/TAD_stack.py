# Pila para hacer las pruebas: 
b = [1, 2, 3, 4, 5, 34, {} , 'hola']

# Crear una pila:
def create_stack():
    stack = list()
    return stack
#create_stack()

# Apilar un elemento:
def stack(name_stack, element):
    return name_stack.append(element)

# Desapilar un elemento:
def unstack(name_stack):
    if len(name_stack) == 0:
        return 'No es posible desapilar un elemento, la pila esta vacia'
    else:
        return name_stack.pop()
#print(unstack(b))

# Tamaño pila:
def size_stack(name_stack):
    return len(name_stack)

# Es vacía:
def isempty(name_stack):
    if len(name_stack) == 0:
        return True
    else: 
        return False

# Recuperar el top de la pila:
def top_stack(name_stack):
    if not isempty(name_stack):
        top = unstack(name_stack)
        stack(name_stack, top)
        return top
    else:
        return 'Pila vacia'
#print(top_stack(b))
#print(b)