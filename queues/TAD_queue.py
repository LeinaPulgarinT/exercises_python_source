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

b = create_queue()
# Retirar un elemento de la cola:
def remove_element_queue(queue):
    if len(queue) == 0:
        return 'La cola esta vacia'
    else:
        return queue.popleft()
#print(remove_element_queue(b))

# Tamaño de la cola
def size_queue(queue):
    return len(queue)
#print(size_queue(b)



# Es vacia:
def isempty_queue(queue):
    if size_queue(queue) == 0:
        return True
    else:
        return False
#print(empty_queue(b))

# Recuperar el frente de la cola:
def front_queue(queue):
    if not isempty_queue(queue):
        front = remove_element_queue(queue)
        queue_aux = create_queue()
        add_queue(queue_aux, front)
        while not isempty_queue(queue):
            front_aux = remove_element_queue(queue)
            add_queue(queue_aux, front_aux)
        while not isempty_queue(queue_aux):
            front_aux_two = remove_element_queue(queue_aux)
            add_queue(queue, front_aux_two)
        return front
    else:
        return 'La cola esta vacia'
print(front_queue(a))
# Verifico que la cola me haya quedado igual
print(a)



