from TAD_stack import create_stack
from TAD_stack import isempty
from TAD_stack import unstack
from TAD_stack import stack

# Pila para hacer las pruebas: 
b = [1, 2, 3, 4, 5, 34, 50]

# Imprimir la pila:
def print_stack(name_stack):
    stack_aux = create_stack()
    while not isempty(name_stack):
        element = unstack(name_stack)
        print(element)
        stack(stack_aux, element)
    
    while not isempty(stack_aux):
        element_aux = unstack(stack_aux)
        stack(name_stack, element_aux)
print_stack(b)
# Imprimo mi pila de pruebas para verificar que si quedo igual:
print(b)