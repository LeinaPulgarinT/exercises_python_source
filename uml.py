# faltan las relaciones de agregacion
class Node():
    def __init__(self):
        self.key = None
        self.value = None
        self.node_left = None
        self.node_right = None

class Tree:
    def __init__(self):
        self.node = Node()
    
    def find(self, key):
        pass

    def add(self, key, value):
        pass


class Key:
    def __init__(self, node):
        self.node = node

    def is_equal(self, key):
        self.key = key
        
    
    def is_less_than(self, key):
        self.key = key
        
class PersonKey(Key):
    def __init__(self, person, node):
        super().__init__(node)
        self.person_key = person

    def value():
        pass

class StrKey(Key):
    def __init__(self, thing, node):
        super().__init__(node)
        self.thing = thing

    def value():
        pass 


class Value:
    def __init__(self, node):
        self.node = node

    def value():
        pass

class PersonValue(Value):
    def __init__(self, person, node):
        super().__init__(node)
        self.person_value = person

class StringValue(Value):
    def __init__(self, thing, node):
        super().__init__(node)
        self.thing = thing

my_person = PersonValue('leina', 'a node')
print(my_person.node)