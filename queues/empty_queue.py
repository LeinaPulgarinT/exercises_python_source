from collections import deque
from TAD_queue import remove_element_queue
from TAD_queue import size_queue
from TAD_queue import add_queue

# Cola para hacer las pruebas:
c = deque([1, 3, 4, 7])

def empty_queue(queue):
    for i in range(size_queue(queue)):
        element = remove_element_queue(queue)
    return queue
print(empty_queue(c))
# Verifico que la cola si haya quedado vacia: 
print(c)