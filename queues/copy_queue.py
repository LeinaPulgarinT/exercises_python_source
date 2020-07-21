from collections import deque 
from TAD_queue import add_queue
from TAD_queue import remove_element_queue
from TAD_queue import isempty_queue

# Cola para hacer las pruebas: 
cola = deque([1, 3, 45, 67])

# Algoritmo que me retorna la copia de una cola: 
def copy_queue(queue_orig):
    queue_aux = deque()
    queue_copy = deque()
    while not isempty_queue(queue_orig):
        element = remove_element_queue(queue_orig)
        add_queue(queue_aux, element)
    while not isempty_queue(queue_aux):
        element_aux = remove_element_queue(queue_aux)
        add_queue(queue_copy, element_aux)
        add_queue(queue_orig, element_aux)
    return queue_copy
print(copy_queue(cola))
# Verifico que la cola original me quede igual:
print(cola)