from collections import deque
queues = deque(['Leina', 'es', 'estudiante', 'de software'])
a = queues.pop()
#print(a)
b = queues.popleft()
print(b)
#print(type(queues))