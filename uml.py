# faltan las relaciones de agregacion
class Node():
    def __init__(self):
        self.key = None
        self.value = None
        self.node_left = None
        self.node_right = None

class Tree:
    node = Node()
    
    def find(self, key):
        pass

    def add(self, key, value):
        pass


class Key:
    node = None

    def is_equal(self, key):
        self.key = key
        
    
    def is_less_than(self, key):
        self.key = key
        
class PersonKey(Key):
    def __init__(self):
        self.persona = None

    def value():
        pass

class StrKey(Key):
    def __init__(self):
        self.thing = ''

    def value():
        pass 


class Value:
    node = None
    def value():
        pass

class PersonValue(Value):
    def __init__(self):
        self.person = None

class StringValue(Value):
    def __init__(self):
        self.thing = ''
