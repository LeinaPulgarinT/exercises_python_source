from TAD_stack import create_stack
from TAD_stack import isempty
from TAD_stack import unstack
from TAD_stack import stack

# Pila para hacer las pruebas: 
b = [1, 2, 3, 4, 5, 34, 50]

# Vaciar pila:
def empty_stack(stack_orig):
    stack_aux = create_stack()
    while not isempty(stack_orig):
        element = unstack(stack_orig)
        stack(stack_aux, element)
    return stack_orig
print(empty_stack(b))
# Imprimo mi pila de pruebas para verificar que si se vacio:
print(b)