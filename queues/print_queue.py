from collections import deque
from TAD_queue import remove_element_queue
from TAD_queue import size_queue
from TAD_queue import add_queue

# Cola para hacer las pruebas:
c = deque([1, 3, 4, 7])

# Algoritmo que me imprime los elementos de una cola:
def print_queue(queue):
    queue_aux = deque()
    for i in range(size_queue(queue)):
        element = remove_element_queue(queue)
        print(element)
        add_queue(queue_aux, element)
    for i in range(size_queue(queue_aux)):
        element_aux = remove_element_queue(queue_aux)
        add_queue(queue, element_aux)
print_queue(c)
# Verifico que mi pila original si me haya quedado igual: 
print(c)
