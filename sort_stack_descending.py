from TAD_stack import create_stack
from TAD_stack import isempty
from TAD_stack import unstack
from TAD_stack import stack
from TAD_stack import top_stack

# Pila para hacer las pruebas: 
c = [ 4, 5, 8, 5, 2, 1, 0, 6, 9, 12]
# Ordenar pila en orden descendente:
def descending_sort(stack_input):
    stack_out = create_stack()
    stack_aux = create_stack()
    stack_aux_two = create_stack()
    def copy_stack(stack_orig, stack_copy):
        tack_aux = create_stack()
        while not isempty(stack_orig):
            element = unstack(stack_orig)
            stack(stack_aux, element)
   
        while not isempty(stack_aux):
            element_aux = unstack(stack_aux)
            stack(stack_copy, element_aux)
            stack(stack_orig, element_aux)
        return stack_copy
    copy_stack(stack_input, stack_aux_two)
    while not isempty(stack_input):
        element = unstack(stack_input)
        def insert(element, stack_sort, stack_aux):
            if isempty(stack_sort) or element <= top_stack(stack_sort):
                stack(stack_sort, element)
                while not isempty(stack_aux):
                    stack(stack_sort, unstack(stack_aux))
            else:
                element_aux = unstack(stack_sort)
                stack(stack_aux, element_aux)
                insert(element, stack_sort, stack_aux)
        insert(element, stack_out, stack_aux)
    copy_stack(stack_aux_two, stack_input)
    return stack_out
print(descending_sort(c))
# Imprimo mi pila de pruebas para verificar que si quedo igual:
print(c)