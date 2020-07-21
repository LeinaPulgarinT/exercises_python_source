from TAD_stack import create_stack
from TAD_stack import isempty
from TAD_stack import unstack
from TAD_stack import stack

# Pilas para hacer las pruebas: 
a = [1, 2, 3, 4, 5, 34, 50]
b = create_stack()
# Copiar una pila:
def copy_stack(stack_orig, stack_copy):
    stack_aux = create_stack()
    while not isempty(stack_orig):
        element = unstack(stack_orig)
        stack(stack_aux, element)
   
    while not isempty(stack_aux):
        element_aux = unstack(stack_aux)
        stack(stack_copy, element_aux)
        stack(stack_orig, element_aux)
    return stack_copy
print(copy_stack(a, b))
# Imprimo mi pila de pruebas para verificar que si quedo igual:
print(a)