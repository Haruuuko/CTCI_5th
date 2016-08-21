from LinkedList import *

class AnimalQueue:
    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()

    def enqueue(self, animal, order):
        if animal == 'dog':
            self.dogs.addNode(animal, order)
        elif animal == 'cat':
            self.cats.addNode(animal, order)

    def dequeueAny(self):
        if self.dogs.head.value < self.cats.head.value:
            return self.dequeueDog()
        else:
            return self.dequeueDog()

    def dequeueDog(self):
        animal = self.dogs.head
        if self.dogs.head:
            self.dogs.removeHead()
        return animal

    def dequeueCat(self):
        animal = self.cats.head
        if self.cats.head:
            self.cats.removeHead()
        return animal

animals = AnimalQueue()
animals.enqueue('dog', 1)
animals.enqueue('cat', 2)
animals.enqueue('dog', 3)
animals.enqueue('dog', 4)
animals.enqueue('cat', 5)
print(animals.dequeueAny())
print(animals.dequeueCat())
print(animals.dequeueDog())



