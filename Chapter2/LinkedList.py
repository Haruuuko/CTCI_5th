from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

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

    def addNode(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def removeNode(self, value):
        current = self.head
        if current.value == value:
            self.head = self.head.next
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                break
            else:
                current = current.next

    def generate(self, n, minv, maxv):
        self.head = self.tail = None
        for i in range(n):
            self.addNode(randint(minv, maxv))
        return self
