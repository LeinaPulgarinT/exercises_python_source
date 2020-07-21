from TAD_stack import create_stack
from TAD_stack import isempty
from TAD_stack import unstack
from TAD_stack import stack

# Pila para hacer las pruebas: 
c = [ 4, 5, 8, 5, 2, 1, 0, 6, 9, 12]
b = create_stack()
# Invertir los elementos de una pila y guardarlos en otra: 
def invert_stack(name_stack, stack_invert):
    stack_aux = create_stack()
    stack_aux_two = create_stack()
    while not isempty(name_stack):
        element = unstack(name_stack)
        stack(stack_aux, element)
    while not isempty(stack_aux):
        element_aux = unstack(stack_aux)
        stack(stack_aux_two, element_aux)
        stack(name_stack, element_aux)
    while not isempty(stack_aux_two):
        element_aux_two = unstack(stack_aux_two)
        stack(stack_invert, element_aux_two)
    return stack_invert

print(invert_stack(c, b))
# Imprimo la pila original para verificar que haya quedado igual:
print(c)
