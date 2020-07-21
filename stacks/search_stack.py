from TAD_stack import create_stack
from TAD_stack import isempty
from TAD_stack import unstack
from TAD_stack import stack

# Pila para hacer las pruebas: 
b = [1, 2, 3, 4, 5, 34, 50]

# Hacer una busqueda dentro de una pila:
def search_stack(name_stack, search_element):
    stack_aux = create_stack()
    found_item = 0 
    while not isempty(name_stack):
        element = unstack(name_stack)
        if element != search_element:
            stack(stack_aux, element)
        else:
            stack(name_stack, element)
            break
    while not isempty(stack_aux):
        element_aux = unstack(stack_aux)
        stack(name_stack, element_aux)
    
    return element
print(search_stack(b, 5))
# Imprimo mi pila de pruebas para verificar que si quedo igual:
print(b)