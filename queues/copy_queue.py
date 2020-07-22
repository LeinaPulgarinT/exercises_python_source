from collections import deque 
from TAD_queue import add_queue
from TAD_queue import remove_element_queue
from TAD_queue import isempty_queue

# Cola para hacer las pruebas: 
queue = deque([1, 3, 45, 67])
# Algoritmo que me copia un cola en otra y me retorna la copia de la cola: 
queue_copy = deque()
def copy_queue(queue_orig, queue_copy):
    queue_aux = deque()
    while not isempty_queue(queue_orig):
        element = remove_element_queue(queue_orig)
        add_queue(queue_aux, element)
    while not isempty_queue(queue_aux):
        element_aux = remove_element_queue(queue_aux)
        add_queue(queue_copy, element_aux)
        add_queue(queue_orig, element_aux)
    return queue_copy
#print(copy_queue(queue, queue_copy))
# Verifico que la cola original me quede igual:
#print(queue)