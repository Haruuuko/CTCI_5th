from random import randint

class Node:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value) + str(self.type)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head is None: return ""
        current = self.head
        values = [str(current.value)]
        while current.next:
            current = current.next
            values.append(str(current.value))
        return ' -> '.join(values)

    def addNode(self, type, value):
        node = Node(type, value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def removeHead(self):
        self.head = self.head.next 
