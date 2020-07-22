from collections import deque
from TAD_queue import isempty_queue
from TAD_queue import remove_element_queue
from TAD_queue import size_queue
from TAD_queue import add_queue
from copy_queue import copy_queue
# Cola para hacer las pruebas:
c = deque([1, 3, 4, 7])
# Algoritmo que me busca un elemento en una cola:
def search_queue(queue, element_search):
    queue_aux = deque()
    while size_queue(queue) != 0:
        element = remove_element_queue(queue)
        if element != element_search:
            add_queue(queue_aux, element)
        else:
            add_queue(queue_aux, element)
            break
    while not isempty_queue(queue):
        element_aux = remove_element_queue(queue)
        add_queue(queue_aux, element_aux)
    copy_queue(queue_aux, queue)
    return element    
print(search_queue(c, 7))
# Verifico que la cola original quede igual:
print(c)
