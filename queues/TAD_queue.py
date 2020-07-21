from collections import deque 
a = deque([1, 4, 8, 12])

# Crear una cola sin la libreria:
def create_queue():
    queue = deque()
    return queue

# Agregar un elemento a la cola:
def add_queue(queue, element):
    queue.append(element)
    return queue

# Retirar un elemento de la cola:
def remove_element_queue(queue):
    queue.popleft()
    return queue
#print(remove_element_queue(a))

# Tamaño de la cola
def size_queue(queue):
    return len(queue)
#b = create_queue()
#print(size_queue(b))

# Es vacia:
def isempty_queue(queue):
    if size_queue(queue) == 0:
        return True
    else:
        return False
#print(empty_queue(b))

# Recuperar el frente de la cola:
def front_queue(queue):
    front = remove_element_queue(queue)
    queue_aux = create_queue()
    add_queue(queue_aux, front)
    while not isempty_queue(queue):
        front_aux = remove_element_queue(queue)
        add_queue(queue_aux, front_aux)
    queue_aux_two = create_queue()
    while not isempty_queue(queue_aux):
        front_aux_two = remove_element_queue(queue_aux)
        add_queue(queue, front_aux_two)
    return front
#print(front_queue(a))
#print(a)



