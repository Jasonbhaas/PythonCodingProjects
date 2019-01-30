class StackWithMax():
    def __init__(self, value):
        self.max = Node(value)
        self.top = Node(value)
    
    def push(self, value):
        if self.max.value <= value:
            self.max.next = Node(value, self.max)
        else:
            self.max.next = Node(self.max.value, self.max)
        self.max = self.max.next

        self.top.next = Node(value, self.top)
        self.top = self.top.next

    def pop(self):
        if (self.top):
            result = self.top.value
            self.max = self.max.previous
            self.top = self.top.previous
        else:
            result = None
        return result
    
    def peek(self):
        return self.top.value

    def getMax(self):
        return self.max.value

    

class Node():
    def __init__(self, value, previous = None, nextNode = None):
        self.previous = previous
        self.next = nextNode
        self.value = value

